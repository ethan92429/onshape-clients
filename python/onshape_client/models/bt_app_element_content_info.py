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


class BTAppElementContentInfo(object):
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
        'change_id': 'str',
        'data': 'list[BTAppElementContentEntryInfo]',
        'error_code': 'int',
        'error_value': 'str',
        'error_description': 'str'
    }

    attribute_map = {
        'change_id': 'changeId',
        'data': 'data',
        'error_code': 'errorCode',
        'error_value': 'errorValue',
        'error_description': 'errorDescription'
    }

    def __init__(self, change_id=None, data=None, error_code=None, error_value=None, error_description=None):  # noqa: E501
        """BTAppElementContentInfo - a model defined in OpenAPI"""  # noqa: E501

        self._change_id = None
        self._data = None
        self._error_code = None
        self._error_value = None
        self._error_description = None
        self.discriminator = None

        if change_id is not None:
            self.change_id = change_id
        if data is not None:
            self.data = data
        if error_code is not None:
            self.error_code = error_code
        if error_value is not None:
            self.error_value = error_value
        if error_description is not None:
            self.error_description = error_description

    @property
    def change_id(self):
        """Gets the change_id of this BTAppElementContentInfo.  # noqa: E501


        :return: The change_id of this BTAppElementContentInfo.  # noqa: E501
        :rtype: str
        """
        return self._change_id

    @change_id.setter
    def change_id(self, change_id):
        """Sets the change_id of this BTAppElementContentInfo.


        :param change_id: The change_id of this BTAppElementContentInfo.  # noqa: E501
        :type: str
        """

        self._change_id = change_id

    @property
    def data(self):
        """Gets the data of this BTAppElementContentInfo.  # noqa: E501


        :return: The data of this BTAppElementContentInfo.  # noqa: E501
        :rtype: list[BTAppElementContentEntryInfo]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BTAppElementContentInfo.


        :param data: The data of this BTAppElementContentInfo.  # noqa: E501
        :type: list[BTAppElementContentEntryInfo]
        """

        self._data = data

    @property
    def error_code(self):
        """Gets the error_code of this BTAppElementContentInfo.  # noqa: E501


        :return: The error_code of this BTAppElementContentInfo.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this BTAppElementContentInfo.


        :param error_code: The error_code of this BTAppElementContentInfo.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def error_value(self):
        """Gets the error_value of this BTAppElementContentInfo.  # noqa: E501


        :return: The error_value of this BTAppElementContentInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_value

    @error_value.setter
    def error_value(self, error_value):
        """Sets the error_value of this BTAppElementContentInfo.


        :param error_value: The error_value of this BTAppElementContentInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "TRANSACTION_CONFLICT", "NOT_FOUND", "INCONSISTENT_CHANGES"]  # noqa: E501
        if error_value not in allowed_values:
            raise ValueError(
                "Invalid value for `error_value` ({0}), must be one of {1}"  # noqa: E501
                .format(error_value, allowed_values)
            )

        self._error_value = error_value

    @property
    def error_description(self):
        """Gets the error_description of this BTAppElementContentInfo.  # noqa: E501


        :return: The error_description of this BTAppElementContentInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this BTAppElementContentInfo.


        :param error_description: The error_description of this BTAppElementContentInfo.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

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
        if not isinstance(other, BTAppElementContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
