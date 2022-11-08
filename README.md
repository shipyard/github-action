# Shipyard Github Action

[![GitHub License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/shipyard/github-action/master/LICENSE) [![Github Action Community](https://img.shields.io/badge/community-Github%20Actions%20Discuss-343434.svg)](https://github.community/c/github-ecosystem/github-apps/64)

Use Github Action to run jobs on ephemeral environments automatically deployed by Shipyard, authenticating into them via a bypass token.
This job connects with Shipyard during a Github Action job, fetching necessary environment variables in order to run e2e tests where authentication via OAuth is normally required.

## How to use

In your Github Workflow file located in `.github/workflows/`, you can use the Shipyard's Github Action as per the following example:

```
on: [pull_request]

jobs:
  cypress-e2e-tests:
    runs-on: ubuntu-latest
    name: Collect the bypass token and URL for an authenticated ephemeral environment attached to this PR in order to run e2e tests on it.
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Fetch Shipyard Tokens
        uses: shipyard/github-action/fetch-shipyard-env@1.0.0
        env:
          SHIPYARD_API_TOKEN: ${{ secrets.SHIPYARD_API_TOKEN }}
      - name: Run the e2e tests on the ephemeral environment
        run: npm run test
        shell: bash
        env:
            CYPRESS_BASE_URL: $SHIPYARD_ENVIRONMENT_URL
            CYPRESS_BYPASS_TOKEN: $SHIPYARD_BYPASS_TOKEN
        
```

The Github Action can be configured by passing inputs or environment variables:

**Inputs**
```
  - name: Fetch Shipyard Tokens
    uses: shipyard/github-action/fetch-shipyard-env@1.0.0
    with:
        api-token: ${{ secrets.SHIPYARD_API_TOKEN }}
        timeout-minutes: 30
```

| Input name | Description | Default Value |
| --------------- | --------------- |--------------- |
| `api-token` | Token required to connect to Shipyard's APIs. Can be obtained from your Organization's setting page | -|
| `timeout-minutes` | Number of minutes to wait for Shipyard environment before timing out. | 60|
| `app-name` | Filter the environments by name of the application on the Shipyard app. | -|


**Environment Variables**
```
  - name: Fetch Shipyard Tokens
    uses: shipyard/github-action/fetch-shipyard-env@1.0.0
    env:
      SHIPYARD_API_TOKEN: ${{ secrets.SHIPYARD_API_TOKEN }}
      SHIPYARD_TIMEOUT: 30
      INPUT_APP_NAME: 'react-app'
```

| Environment Variable | Description | Default Value |
| --------------- | --------------- |--------------- |
| `SHIPYARD_API_TOKEN` | Token required to connect to Shipyard's APIs. Can be obtained from your Organization's setting page  |-|
| `SHIPYARD_TIMEOUT` | Number of minutes to wait for Shipyard environment before timing out. |60|
| `SHIPYARD_APP_NAME` | Filter the environments by name of the application on the Shipyard app. |-|

**NOTE**: Inputs are given precedence over environment variables.

If input `api-token` or environment variable `SHIPYARD_API_TOKEN` is not provided, error is raised.

On successful run, the following environment variables are set, which can then be passed on to other actions in the same workflow.

| Parameter Name | Description |
| --------------- | --------------- |
|`SHIPYARD_ENVIRONMENT_URL` | URL of the ephemeral environment |
|`SHIPYARD_ENVIRONMENT_ID`  | ID of the ephemeral environment  |
|`SHIPYARD_BYPASS_TOKEN`    | Token to bypass authentication   |


## Resources

[Shipyard Documentation](https://docs.shipyard.build/docs/)