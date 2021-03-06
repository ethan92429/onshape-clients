# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.97
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTBelScriptLibraryVersion(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'major': 'int',
        'minor': 'int',
        'valid': 'bool',
        'version_number': 'int',
        'point': 'int'
    }

    attribute_map = {
        'major': 'major',
        'minor': 'minor',
        'valid': 'valid',
        'version_number': 'versionNumber',
        'point': 'point'
    }

    def __init__(self, major=None, minor=None, valid=None, version_number=None, point=None):  # noqa: E501
        """BTBelScriptLibraryVersion - a model defined in OpenAPI"""  # noqa: E501

        self._major = None
        self._minor = None
        self._valid = None
        self._version_number = None
        self._point = None
        self.discriminator = None

        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if valid is not None:
            self.valid = valid
        if version_number is not None:
            self.version_number = version_number
        if point is not None:
            self.point = point

    @property
    def major(self):
        """Gets the major of this BTBelScriptLibraryVersion.  # noqa: E501


        :return: The major of this BTBelScriptLibraryVersion.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this BTBelScriptLibraryVersion.


        :param major: The major of this BTBelScriptLibraryVersion.  # noqa: E501
        :type: int
        """

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this BTBelScriptLibraryVersion.  # noqa: E501


        :return: The minor of this BTBelScriptLibraryVersion.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this BTBelScriptLibraryVersion.


        :param minor: The minor of this BTBelScriptLibraryVersion.  # noqa: E501
        :type: int
        """

        self._minor = minor

    @property
    def valid(self):
        """Gets the valid of this BTBelScriptLibraryVersion.  # noqa: E501


        :return: The valid of this BTBelScriptLibraryVersion.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this BTBelScriptLibraryVersion.


        :param valid: The valid of this BTBelScriptLibraryVersion.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def version_number(self):
        """Gets the version_number of this BTBelScriptLibraryVersion.  # noqa: E501


        :return: The version_number of this BTBelScriptLibraryVersion.  # noqa: E501
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this BTBelScriptLibraryVersion.


        :param version_number: The version_number of this BTBelScriptLibraryVersion.  # noqa: E501
        :type: int
        """

        self._version_number = version_number

    @property
    def point(self):
        """Gets the point of this BTBelScriptLibraryVersion.  # noqa: E501


        :return: The point of this BTBelScriptLibraryVersion.  # noqa: E501
        :rtype: int
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this BTBelScriptLibraryVersion.


        :param point: The point of this BTBelScriptLibraryVersion.  # noqa: E501
        :type: int
        """

        self._point = point

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTBelScriptLibraryVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
