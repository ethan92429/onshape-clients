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


class Definition(object):
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
        'name': 'str',
        'description': 'str',
        'code': 'int',
        'sort_order': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'code': 'code',
        'sort_order': 'sortOrder'
    }

    def __init__(self, name=None, description=None, code=None, sort_order=None):  # noqa: E501
        """Definition - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._description = None
        self._code = None
        self._sort_order = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if code is not None:
            self.code = code
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def name(self):
        """Gets the name of this Definition.  # noqa: E501


        :return: The name of this Definition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Definition.


        :param name: The name of this Definition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Definition.  # noqa: E501


        :return: The description of this Definition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Definition.


        :param description: The description of this Definition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def code(self):
        """Gets the code of this Definition.  # noqa: E501


        :return: The code of this Definition.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Definition.


        :param code: The code of this Definition.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def sort_order(self):
        """Gets the sort_order of this Definition.  # noqa: E501


        :return: The sort_order of this Definition.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this Definition.


        :param sort_order: The sort_order of this Definition.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

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
        if not isinstance(other, Definition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
