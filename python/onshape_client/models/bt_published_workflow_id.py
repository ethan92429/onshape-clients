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


class BTPublishedWorkflowId(object):
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
        'company_id': 'str',
        'workflow_id': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'company_id': 'companyId',
        'workflow_id': 'workflowId',
        'version_id': 'versionId'
    }

    def __init__(self, company_id=None, workflow_id=None, version_id=None):  # noqa: E501
        """BTPublishedWorkflowId - a model defined in OpenAPI"""  # noqa: E501

        self._company_id = None
        self._workflow_id = None
        self._version_id = None
        self.discriminator = None

        if company_id is not None:
            self.company_id = company_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if version_id is not None:
            self.version_id = version_id

    @property
    def company_id(self):
        """Gets the company_id of this BTPublishedWorkflowId.  # noqa: E501


        :return: The company_id of this BTPublishedWorkflowId.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTPublishedWorkflowId.


        :param company_id: The company_id of this BTPublishedWorkflowId.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this BTPublishedWorkflowId.  # noqa: E501


        :return: The workflow_id of this BTPublishedWorkflowId.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this BTPublishedWorkflowId.


        :param workflow_id: The workflow_id of this BTPublishedWorkflowId.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def version_id(self):
        """Gets the version_id of this BTPublishedWorkflowId.  # noqa: E501


        :return: The version_id of this BTPublishedWorkflowId.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTPublishedWorkflowId.


        :param version_id: The version_id of this BTPublishedWorkflowId.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

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
        if not isinstance(other, BTPublishedWorkflowId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
