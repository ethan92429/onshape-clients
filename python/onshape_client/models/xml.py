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


class XML(object):
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
        'namespace': 'str',
        'prefix': 'str',
        'attribute': 'bool',
        'wrapped': 'bool',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'prefix': 'prefix',
        'attribute': 'attribute',
        'wrapped': 'wrapped',
        'extensions': 'extensions'
    }

    def __init__(self, name=None, namespace=None, prefix=None, attribute=None, wrapped=None, extensions=None):  # noqa: E501
        """XML - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._namespace = None
        self._prefix = None
        self._attribute = None
        self._wrapped = None
        self._extensions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if prefix is not None:
            self.prefix = prefix
        if attribute is not None:
            self.attribute = attribute
        if wrapped is not None:
            self.wrapped = wrapped
        if extensions is not None:
            self.extensions = extensions

    @property
    def name(self):
        """Gets the name of this XML.  # noqa: E501


        :return: The name of this XML.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XML.


        :param name: The name of this XML.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this XML.  # noqa: E501


        :return: The namespace of this XML.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this XML.


        :param namespace: The namespace of this XML.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def prefix(self):
        """Gets the prefix of this XML.  # noqa: E501


        :return: The prefix of this XML.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this XML.


        :param prefix: The prefix of this XML.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def attribute(self):
        """Gets the attribute of this XML.  # noqa: E501


        :return: The attribute of this XML.  # noqa: E501
        :rtype: bool
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this XML.


        :param attribute: The attribute of this XML.  # noqa: E501
        :type: bool
        """

        self._attribute = attribute

    @property
    def wrapped(self):
        """Gets the wrapped of this XML.  # noqa: E501


        :return: The wrapped of this XML.  # noqa: E501
        :rtype: bool
        """
        return self._wrapped

    @wrapped.setter
    def wrapped(self, wrapped):
        """Sets the wrapped of this XML.


        :param wrapped: The wrapped of this XML.  # noqa: E501
        :type: bool
        """

        self._wrapped = wrapped

    @property
    def extensions(self):
        """Gets the extensions of this XML.  # noqa: E501


        :return: The extensions of this XML.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this XML.


        :param extensions: The extensions of this XML.  # noqa: E501
        :type: dict(str, object)
        """

        self._extensions = extensions

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
        if not isinstance(other, XML):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
