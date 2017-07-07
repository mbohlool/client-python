# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NFSVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, path=None, read_only=None, server=None):
        """
        V1NFSVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'path': 'str',
            'read_only': 'bool',
            'server': 'str'
        }

        self.attribute_map = {
            'path': 'path',
            'read_only': 'readOnly',
            'server': 'server'
        }

        self._path = path
        self._read_only = read_only
        self._server = server

    @property
    def path(self):
        """
        Gets the path of this V1NFSVolumeSource.
        Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

        :return: The path of this V1NFSVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1NFSVolumeSource.
        Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

        :param path: The path of this V1NFSVolumeSource.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def read_only(self):
        """
        Gets the read_only of this V1NFSVolumeSource.
        ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

        :return: The read_only of this V1NFSVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1NFSVolumeSource.
        ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

        :param read_only: The read_only of this V1NFSVolumeSource.
        :type: bool
        """

        self._read_only = read_only

    @property
    def server(self):
        """
        Gets the server of this V1NFSVolumeSource.
        Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

        :return: The server of this V1NFSVolumeSource.
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """
        Sets the server of this V1NFSVolumeSource.
        Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

        :param server: The server of this V1NFSVolumeSource.
        :type: str
        """
        if server is None:
            raise ValueError("Invalid value for `server`, must not be `None`")

        self._server = server

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1NFSVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
