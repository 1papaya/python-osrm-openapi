# coding: utf-8

"""
    OSRM API v5.22.0

    Open Source Routing Machine API  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import osrm_openapi
from osrm_openapi.api.osrm_api import OSRMApi  # noqa: E501
from osrm_openapi.rest import ApiException


class TestOSRMApi(unittest.TestCase):
    """OSRMApi unit test stubs"""

    def setUp(self):
        self.api = osrm_openapi.api.osrm_api.OSRMApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_nearest(self):
        """Test case for nearest

        """
        pass


if __name__ == '__main__':
    unittest.main()