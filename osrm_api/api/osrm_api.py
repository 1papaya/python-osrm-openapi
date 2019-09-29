# coding: utf-8

"""
    OSRM API v5.22.0

    Open Source Routing Machine API  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from osrm_api.api_client import ApiClient
from osrm_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class OSRMApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def nearest(self, version, profile, coordinates, number, **kwargs):  # noqa: E501
        """nearest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.nearest(version, profile, coordinates, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str version: (required)
        :param str profile: (required)
        :param str coordinates: (required)
        :param int number: (required)
        :param str bearings:
        :param str radiuses:
        :param bool generate_hints:
        :param str hints:
        :param str approaches:
        :param str exclude:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.nearest_with_http_info(version, profile, coordinates, number, **kwargs)  # noqa: E501

    def nearest_with_http_info(self, version, profile, coordinates, number, **kwargs):  # noqa: E501
        """nearest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.nearest_with_http_info(version, profile, coordinates, number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str version: (required)
        :param str profile: (required)
        :param str coordinates: (required)
        :param int number: (required)
        :param str bearings:
        :param str radiuses:
        :param bool generate_hints:
        :param str hints:
        :param str approaches:
        :param str exclude:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['version', 'profile', 'coordinates', 'number', 'bearings', 'radiuses', 'generate_hints', 'hints', 'approaches', 'exclude']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method nearest" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in local_var_params or
                local_var_params['version'] is None):
            raise ApiValueError("Missing the required parameter `version` when calling `nearest`")  # noqa: E501
        # verify the required parameter 'profile' is set
        if ('profile' not in local_var_params or
                local_var_params['profile'] is None):
            raise ApiValueError("Missing the required parameter `profile` when calling `nearest`")  # noqa: E501
        # verify the required parameter 'coordinates' is set
        if ('coordinates' not in local_var_params or
                local_var_params['coordinates'] is None):
            raise ApiValueError("Missing the required parameter `coordinates` when calling `nearest`")  # noqa: E501
        # verify the required parameter 'number' is set
        if ('number' not in local_var_params or
                local_var_params['number'] is None):
            raise ApiValueError("Missing the required parameter `number` when calling `nearest`")  # noqa: E501

        if 'number' in local_var_params and local_var_params['number'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `number` when calling `nearest`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']  # noqa: E501
        if 'profile' in local_var_params:
            path_params['profile'] = local_var_params['profile']  # noqa: E501
        if 'coordinates' in local_var_params:
            path_params['coordinates'] = local_var_params['coordinates']  # noqa: E501

        query_params = []
        if 'bearings' in local_var_params:
            query_params.append(('bearings', local_var_params['bearings']))  # noqa: E501
        if 'radiuses' in local_var_params:
            query_params.append(('radiuses', local_var_params['radiuses']))  # noqa: E501
        if 'generate_hints' in local_var_params:
            query_params.append(('generate_hints', local_var_params['generate_hints']))  # noqa: E501
        if 'hints' in local_var_params:
            query_params.append(('hints', local_var_params['hints']))  # noqa: E501
        if 'approaches' in local_var_params:
            query_params.append(('approaches', local_var_params['approaches']))  # noqa: E501
        if 'exclude' in local_var_params:
            query_params.append(('exclude', local_var_params['exclude']))  # noqa: E501
        if 'number' in local_var_params:
            query_params.append(('number', local_var_params['number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nearest/{version}/{profile}/{coordinates}.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)