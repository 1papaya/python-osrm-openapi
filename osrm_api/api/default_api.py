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


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def route(self, version, profile, coordinates, **kwargs):  # noqa: E501
        """route  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.route(version, profile, coordinates, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str version: Version of the protocol implemented by the service. v1 for all OSRM 5.x installations (required)
        :param str profile: Mode of transportation, is determined statically by the Lua profile that is used to prepare the data using osrm-extract. Typically car, bike or foot if using one of the supplied profiles. (required)
        :param str coordinates: (required)
        :param str bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction.
        :param str radiuses: Limits the search to given radius in meters.
        :param bool generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter.
        :param str hints: Hint from previous request to derive position in street network.
        :param str approaches: Keep waypoints on curb side.
        :param str exclude: Additive list of classes to avoid, order does not matter.
        :param OneOfbooleaninteger alternatives: Search for alternative routes. Passing a number alternatives=n searches for up to n alternative routes.
        :param bool steps: Returned route steps for each route leg
        :param bool annotations: Returns additional metadata for each coordinate along the route geometry.
        :param str geometries: Returned route geometry format (influences overview and per step)
        :param str overview: Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all.
        :param str continue_straight: Forces the route to keep going straight at waypoints constraining uturns there even if it would be faster. Default value depends on the profile.
        :param str waypoints: Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints.
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
        return self.route_with_http_info(version, profile, coordinates, **kwargs)  # noqa: E501

    def route_with_http_info(self, version, profile, coordinates, **kwargs):  # noqa: E501
        """route  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.route_with_http_info(version, profile, coordinates, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str version: Version of the protocol implemented by the service. v1 for all OSRM 5.x installations (required)
        :param str profile: Mode of transportation, is determined statically by the Lua profile that is used to prepare the data using osrm-extract. Typically car, bike or foot if using one of the supplied profiles. (required)
        :param str coordinates: (required)
        :param str bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction.
        :param str radiuses: Limits the search to given radius in meters.
        :param bool generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter.
        :param str hints: Hint from previous request to derive position in street network.
        :param str approaches: Keep waypoints on curb side.
        :param str exclude: Additive list of classes to avoid, order does not matter.
        :param OneOfbooleaninteger alternatives: Search for alternative routes. Passing a number alternatives=n searches for up to n alternative routes.
        :param bool steps: Returned route steps for each route leg
        :param bool annotations: Returns additional metadata for each coordinate along the route geometry.
        :param str geometries: Returned route geometry format (influences overview and per step)
        :param str overview: Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all.
        :param str continue_straight: Forces the route to keep going straight at waypoints constraining uturns there even if it would be faster. Default value depends on the profile.
        :param str waypoints: Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints.
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

        all_params = ['version', 'profile', 'coordinates', 'bearings', 'radiuses', 'generate_hints', 'hints', 'approaches', 'exclude', 'alternatives', 'steps', 'annotations', 'geometries', 'overview', 'continue_straight', 'waypoints']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method route" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in local_var_params or
                local_var_params['version'] is None):
            raise ApiValueError("Missing the required parameter `version` when calling `route`")  # noqa: E501
        # verify the required parameter 'profile' is set
        if ('profile' not in local_var_params or
                local_var_params['profile'] is None):
            raise ApiValueError("Missing the required parameter `profile` when calling `route`")  # noqa: E501
        # verify the required parameter 'coordinates' is set
        if ('coordinates' not in local_var_params or
                local_var_params['coordinates'] is None):
            raise ApiValueError("Missing the required parameter `coordinates` when calling `route`")  # noqa: E501

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
        if 'alternatives' in local_var_params:
            query_params.append(('alternatives', local_var_params['alternatives']))  # noqa: E501
        if 'steps' in local_var_params:
            query_params.append(('steps', local_var_params['steps']))  # noqa: E501
        if 'annotations' in local_var_params:
            query_params.append(('annotations', local_var_params['annotations']))  # noqa: E501
        if 'geometries' in local_var_params:
            query_params.append(('geometries', local_var_params['geometries']))  # noqa: E501
        if 'overview' in local_var_params:
            query_params.append(('overview', local_var_params['overview']))  # noqa: E501
        if 'continue_straight' in local_var_params:
            query_params.append(('continue_straight', local_var_params['continue_straight']))  # noqa: E501
        if 'waypoints' in local_var_params:
            query_params.append(('waypoints', local_var_params['waypoints']))  # noqa: E501

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
            '/route/{version}/{profile}/{coordinates}.json', 'GET',
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
