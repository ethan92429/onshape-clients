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


class BTUpdateInContextParams(object):
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
        'microversion_id': 'BTMicroversionId',
        'encoded_context_configuration': 'str',
        'use_latest_microversion': 'bool',
        'description': 'str',
        'context_id': 'str'
    }

    attribute_map = {
        'microversion_id': 'microversionId',
        'encoded_context_configuration': 'encodedContextConfiguration',
        'use_latest_microversion': 'useLatestMicroversion',
        'description': 'description',
        'context_id': 'contextId'
    }

    def __init__(self, microversion_id=None, encoded_context_configuration=None, use_latest_microversion=None, description=None, context_id=None):  # noqa: E501
        """BTUpdateInContextParams - a model defined in OpenAPI"""  # noqa: E501

        self._microversion_id = None
        self._encoded_context_configuration = None
        self._use_latest_microversion = None
        self._description = None
        self._context_id = None
        self.discriminator = None

        if microversion_id is not None:
            self.microversion_id = microversion_id
        if encoded_context_configuration is not None:
            self.encoded_context_configuration = encoded_context_configuration
        if use_latest_microversion is not None:
            self.use_latest_microversion = use_latest_microversion
        if description is not None:
            self.description = description
        if context_id is not None:
            self.context_id = context_id

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTUpdateInContextParams.  # noqa: E501


        :return: The microversion_id of this BTUpdateInContextParams.  # noqa: E501
        :rtype: BTMicroversionId
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTUpdateInContextParams.


        :param microversion_id: The microversion_id of this BTUpdateInContextParams.  # noqa: E501
        :type: BTMicroversionId
        """

        self._microversion_id = microversion_id

    @property
    def encoded_context_configuration(self):
        """Gets the encoded_context_configuration of this BTUpdateInContextParams.  # noqa: E501


        :return: The encoded_context_configuration of this BTUpdateInContextParams.  # noqa: E501
        :rtype: str
        """
        return self._encoded_context_configuration

    @encoded_context_configuration.setter
    def encoded_context_configuration(self, encoded_context_configuration):
        """Sets the encoded_context_configuration of this BTUpdateInContextParams.


        :param encoded_context_configuration: The encoded_context_configuration of this BTUpdateInContextParams.  # noqa: E501
        :type: str
        """

        self._encoded_context_configuration = encoded_context_configuration

    @property
    def use_latest_microversion(self):
        """Gets the use_latest_microversion of this BTUpdateInContextParams.  # noqa: E501


        :return: The use_latest_microversion of this BTUpdateInContextParams.  # noqa: E501
        :rtype: bool
        """
        return self._use_latest_microversion

    @use_latest_microversion.setter
    def use_latest_microversion(self, use_latest_microversion):
        """Sets the use_latest_microversion of this BTUpdateInContextParams.


        :param use_latest_microversion: The use_latest_microversion of this BTUpdateInContextParams.  # noqa: E501
        :type: bool
        """

        self._use_latest_microversion = use_latest_microversion

    @property
    def description(self):
        """Gets the description of this BTUpdateInContextParams.  # noqa: E501


        :return: The description of this BTUpdateInContextParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTUpdateInContextParams.


        :param description: The description of this BTUpdateInContextParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def context_id(self):
        """Gets the context_id of this BTUpdateInContextParams.  # noqa: E501


        :return: The context_id of this BTUpdateInContextParams.  # noqa: E501
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """Sets the context_id of this BTUpdateInContextParams.


        :param context_id: The context_id of this BTUpdateInContextParams.  # noqa: E501
        :type: str
        """

        self._context_id = context_id

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
        if not isinstance(other, BTUpdateInContextParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
