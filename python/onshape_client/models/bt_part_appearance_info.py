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


class BTPartAppearanceInfo(object):
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
        'color': 'BTColorInfo',
        'opacity': 'int',
        'is_generated': 'bool'
    }

    attribute_map = {
        'color': 'color',
        'opacity': 'opacity',
        'is_generated': 'isGenerated'
    }

    def __init__(self, color=None, opacity=None, is_generated=None):  # noqa: E501
        """BTPartAppearanceInfo - a model defined in OpenAPI"""  # noqa: E501

        self._color = None
        self._opacity = None
        self._is_generated = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if opacity is not None:
            self.opacity = opacity
        if is_generated is not None:
            self.is_generated = is_generated

    @property
    def color(self):
        """Gets the color of this BTPartAppearanceInfo.  # noqa: E501


        :return: The color of this BTPartAppearanceInfo.  # noqa: E501
        :rtype: BTColorInfo
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this BTPartAppearanceInfo.


        :param color: The color of this BTPartAppearanceInfo.  # noqa: E501
        :type: BTColorInfo
        """

        self._color = color

    @property
    def opacity(self):
        """Gets the opacity of this BTPartAppearanceInfo.  # noqa: E501


        :return: The opacity of this BTPartAppearanceInfo.  # noqa: E501
        :rtype: int
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this BTPartAppearanceInfo.


        :param opacity: The opacity of this BTPartAppearanceInfo.  # noqa: E501
        :type: int
        """

        self._opacity = opacity

    @property
    def is_generated(self):
        """Gets the is_generated of this BTPartAppearanceInfo.  # noqa: E501


        :return: The is_generated of this BTPartAppearanceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_generated

    @is_generated.setter
    def is_generated(self, is_generated):
        """Sets the is_generated of this BTPartAppearanceInfo.


        :param is_generated: The is_generated of this BTPartAppearanceInfo.  # noqa: E501
        :type: bool
        """

        self._is_generated = is_generated

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
        if not isinstance(other, BTPartAppearanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
