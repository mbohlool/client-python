# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_api_version import V1beta1APIVersion


class TestV1beta1APIVersion(unittest.TestCase):
    """ V1beta1APIVersion unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1APIVersion(self):
        """
        Test V1beta1APIVersion
        """
        model = kubernetes.client.models.v1beta1_api_version.V1beta1APIVersion()


if __name__ == '__main__':
    unittest.main()
