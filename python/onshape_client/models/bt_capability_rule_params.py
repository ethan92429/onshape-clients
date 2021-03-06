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


class BTCapabilityRuleParams(object):
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
        'id': 'str',
        'description': 'str',
        'script': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'script': 'script'
    }

    def __init__(self, name=None, id=None, description=None, script=None):  # noqa: E501
        """BTCapabilityRuleParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._id = None
        self._description = None
        self._script = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if script is not None:
            self.script = script

    @property
    def name(self):
        """Gets the name of this BTCapabilityRuleParams.  # noqa: E501


        :return: The name of this BTCapabilityRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTCapabilityRuleParams.


        :param name: The name of this BTCapabilityRuleParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTCapabilityRuleParams.  # noqa: E501


        :return: The id of this BTCapabilityRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTCapabilityRuleParams.


        :param id: The id of this BTCapabilityRuleParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this BTCapabilityRuleParams.  # noqa: E501


        :return: The description of this BTCapabilityRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTCapabilityRuleParams.


        :param description: The description of this BTCapabilityRuleParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def script(self):
        """Gets the script of this BTCapabilityRuleParams.  # noqa: E501


        :return: The script of this BTCapabilityRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this BTCapabilityRuleParams.


        :param script: The script of this BTCapabilityRuleParams.  # noqa: E501
        :type: str
        """

        self._script = script

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
        if not isinstance(other, BTCapabilityRuleParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
