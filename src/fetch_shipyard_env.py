"""
# Purpose:
Wait for the Shipyard environment to be ready,
then put its data in the environment.
# Required environment variables:
- GITHUB_ENV
- GITHUB_REPOSITORY
- GITHUB_REF_NAME
- INPUT_API_TOKEN or SHIPYARD_API_TOKEN
- INPUT_TIMEOUT_MINUTES or SHIPYARD_TIMEOUT
- INPUT_APP_NAME or SHIPYARD_APP_NAME
"""
from __future__ import print_function

import os
import sys
import time
from datetime import datetime, timedelta

import swagger_client
from swagger_client.rest import ApiException


def exit(msg):
    print(msg)
    sys.exit(1)


# Make sure there's a bash env file in the environment
bash_env_path = os.environ.get("GITHUB_ENV")
if not bash_env_path:
    exit("ERROR: missing GITHUB_ENV environment variable")

# Constants
repo_owner = os.environ.get("GITHUB_REPOSITORY_OWNER")
github_repo = os.environ.get("GITHUB_REPOSITORY")  # repo_owner/repo
repo = github_repo.replace(f"{repo_owner}/", "") if github_repo else None
# GITHUB_HEAD_REF - The head ref or source branch of the pull request in a workflow run
branch = os.environ.get("GITHUB_HEAD_REF")
if not branch:
    # GITHUB_REF_NAME - The branch or tag name that triggered the workflow run
    branch = os.environ.get("GITHUB_REF_NAME")
ref_type = os.environ.get("GITHUB_REF_TYPE")  # TODO: handle branch or tag?

# Get auth token
api_token = os.environ.get("INPUT_API_TOKEN")
# if input is not provided, check ENV vars
if not api_token:
    api_token = os.environ.get("SHIPYARD_API_TOKEN")
if not api_token:
    exit("No SHIPYARD_API_TOKEN provided, exiting.")

# Get the timeout
timeout_minutes = os.environ.get("INPUT_TIMEOUT_MINUTES")
if not timeout_minutes:
    timeout_minutes = os.environ.get("SHIPYARD_TIMEOUT")
if timeout_minutes:
    try:
        timeout_minutes = int(timeout_minutes)
    except Exception:
        exit(
            'ERROR: the SHIPYARD_TIMEOUT provided ("{}") is not an integer'.format(
                timeout_minutes
            )
        )
else:
    timeout_minutes = 60

# Get the app name
app_name = os.environ.get("INPUT_APP_NAME")
if not app_name:
    app_name = os.environ.get("SHIPYARD_APP_NAME")

# Prepare API client
configuration = swagger_client.Configuration()
configuration.api_key["x-api-token"] = api_token
client = swagger_client.ApiClient(configuration)
api_instance = swagger_client.EnvironmentApi(client)


def fetch_shipyard_environment():
    """Fetch the Shipyard environment for this Github job"""

    # Hit the Shipyard API
    try:
        args = {
            "repo_owner": repo_owner,
            "repo_name": repo,
            "branch": branch
        }
        if app_name:
            args["name"] = app_name
        response = api_instance.list_environments(**args).to_dict()
    except ApiException as e:
        exit("ERROR: issue while listing environments via API: {}".format(e))

    # Exit if any errors
    errors = response.get("errors")
    if errors:
        exit("ERROR: {}".format(errors[0]["title"]))

    # Verify an environment was found
    if not len(response["data"]):
        exit("ERROR: no matching Shipyard environment found")

    # Verify the data is where we expect
    try:
        environment_id = response["data"][0]["id"]
        environment_data = response["data"][0]["attributes"]
    except Exception:
        exit("ERROR: invalid response data structure")

    # Verify all the needed fields are available
    for param in ("bypass_token", "url", "ready", "stopped", "retired"):
        if param not in environment_data:
            exit("ERROR: no {} found!".format(param))

    return environment_id, environment_data


def restart_environment(environment_id):
    """Restart the Shipyard environment with the provided ID"""

    try:
        api_instance.restart_environment(environment_id)
    except ApiException as e:
        exit("ERROR: issue while restart the environment: {}".format(e))


def wait_for_environment():
    """Return the Shipyard environment data once it's ready"""

    auto_restart = True
    was_restarted = False

    # Check the environment
    environment_id, environment_data = fetch_shipyard_environment()

    start = datetime.now()
    timeout_end = datetime.now() + timedelta(minutes=timeout_minutes)

    # Until the environment is ready
    while not environment_data["ready"]:
        now = datetime.now()
        # Check if the timeout has elapsed
        if datetime.now() > timeout_end:
            exit("{} minute timeout elapsed, exiting!".format(timeout_minutes))

        # Auto-restart the environment once if indicated
        if all([environment_data["retired"], auto_restart, not was_restarted]):
            restart_environment(environment_id)
            was_restarted = True
            print("Restarted Shipyard environment...")
        elif environment_data["stopped"] and not environment_data["processing"]:
            exit("ERROR: this environment is stopped and no builds are processing")

        # Wait 15 seconds
        seconds_waited = int((now - start).total_seconds())
        wait_string = " ({}s elapsed)".format(seconds_waited) if seconds_waited else ""
        print("Waiting for Shipyard environment...{}".format(wait_string))
        time.sleep(15)

        # Check on the environment again
        environment_id, environment_data = fetch_shipyard_environment()

    return environment_id, environment_data


def main():
    """
    Wait for the Shipyard environment to be ready,
    then put it's data in the bash environment.
    """

    environment_id, environment_data = wait_for_environment()

    try:
        # Try to fetch the commit hash of classic environments
        commit_hash = environment_data.get("commit_hash")

        # Fetch the commit hash if this is a single-repo app
        if not commit_hash:
            projects = environment_data.get("projects")
            if len(projects) == 1:
                commit_hash = projects[0]["commit_hash"]
    except Exception:
        print("WARNING: unable to retrieve commit hash")
        commit_hash = None

    # Write the data to the job's environment
    with open(bash_env_path, "a") as bash_env:
        bash_env.write(
            "\n".join(
                [
                    "SHIPYARD_BYPASS_TOKEN={}".format(environment_data["bypass_token"]),
                    "SHIPYARD_ENVIRONMENT_ID={}".format(environment_id),
                    "SHIPYARD_ENVIRONMENT_URL={}".format(environment_data["url"]),
                    "SHIPYARD_ENVIRONMENT_READY={}".format(environment_data["ready"]),
                    "SHIPYARD_ENVIRONMENT_RETIRED={}".format(
                        environment_data["retired"]
                    ),
                ]
                + ["SHIPYARD_ENVIRONMENT_COMMIT_HASH={}".format(commit_hash)]
                if commit_hash
                else []
            )
        )

    print("Shipyard environment data written to {}!".format(bash_env_path))


if __name__ == "__main__":
    main()
