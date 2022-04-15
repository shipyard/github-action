# coding: utf-8

"""
    Shipyard API

    The official OpenAPI spec for the Shipyard API.  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EnvironmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_environment(self, uuid, **kwargs):  # noqa: E501
        """Get an environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_environment(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: the environment's identifying UUID (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_environment_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_environment_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def get_environment_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Get an environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_environment_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: the environment's identifying UUID (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["uuid"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_environment" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'uuid' is set
        if "uuid" not in params or params["uuid"] is None:
            raise ValueError(
                "Missing the required parameter `uuid` when calling `get_environment`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "uuid" in params:
            path_params["uuid"] = params["uuid"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKeyAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/environment/{uuid}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2001",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_environments(self, **kwargs):  # noqa: E501
        """List your organization's environments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_environments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str org_name:
        :param str repo_name:
        :param str branch:
        :param int pull_request_number:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_environments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_environments_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_environments_with_http_info(self, **kwargs):  # noqa: E501
        """List your organization's environments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_environments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str org_name:
        :param str repo_name:
        :param str branch:
        :param int pull_request_number:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "name",
            "org_name",
            "repo_name",
            "branch",
            "pull_request_number",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_environments" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501
        if "org_name" in params:
            query_params.append(("org_name", params["org_name"]))  # noqa: E501
        if "repo_name" in params:
            query_params.append(("repo_name", params["repo_name"]))  # noqa: E501
        if "branch" in params:
            query_params.append(("branch", params["branch"]))  # noqa: E501
        if "pull_request_number" in params:
            query_params.append(
                ("pull_request_number", params["pull_request_number"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKeyAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/environment",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse200",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def restart_environment(self, uuid, **kwargs):  # noqa: E501
        """Restart an environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.restart_environment(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: the environments's identifying UUID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.restart_environment_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.restart_environment_with_http_info(
                uuid, **kwargs
            )  # noqa: E501
            return data

    def restart_environment_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Restart an environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.restart_environment_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: the environments's identifying UUID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["uuid"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method restart_environment" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'uuid' is set
        if "uuid" not in params or params["uuid"] is None:
            raise ValueError(
                "Missing the required parameter `uuid` when calling `restart_environment`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "uuid" in params:
            path_params["uuid"] = params["uuid"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["ApiKeyAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/environment/{uuid}/restart",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def stop_environment(self, uuid, **kwargs):  # noqa: E501
        """Stop an environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop_environment(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: the environments's identifying UUID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.stop_environment_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.stop_environment_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def stop_environment_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Stop an environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop_environment_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: the environments's identifying UUID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["uuid"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_environment" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'uuid' is set
        if "uuid" not in params or params["uuid"] is None:
            raise ValueError(
                "Missing the required parameter `uuid` when calling `stop_environment`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "uuid" in params:
            path_params["uuid"] = params["uuid"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["ApiKeyAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/environment/{uuid}/stop",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )