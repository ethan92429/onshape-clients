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


class BTMetricsListParams(object):
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
        'collected_metrics': 'list[BTMetricParams]'
    }

    attribute_map = {
        'collected_metrics': 'collectedMetrics'
    }

    def __init__(self, collected_metrics=None):  # noqa: E501
        """BTMetricsListParams - a model defined in OpenAPI"""  # noqa: E501

        self._collected_metrics = None
        self.discriminator = None

        if collected_metrics is not None:
            self.collected_metrics = collected_metrics

    @property
    def collected_metrics(self):
        """Gets the collected_metrics of this BTMetricsListParams.  # noqa: E501


        :return: The collected_metrics of this BTMetricsListParams.  # noqa: E501
        :rtype: list[BTMetricParams]
        """
        return self._collected_metrics

    @collected_metrics.setter
    def collected_metrics(self, collected_metrics):
        """Sets the collected_metrics of this BTMetricsListParams.


        :param collected_metrics: The collected_metrics of this BTMetricsListParams.  # noqa: E501
        :type: list[BTMetricParams]
        """

        self._collected_metrics = collected_metrics

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
        if not isinstance(other, BTMetricsListParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
