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
from kubernetes.client.models.v1_toleration import V1Toleration


class TestV1Toleration(unittest.TestCase):
    """ V1Toleration unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Toleration(self):
        """
        Test V1Toleration
        """
        model = kubernetes.client.models.v1_toleration.V1Toleration()


if __name__ == '__main__':
    unittest.main()
