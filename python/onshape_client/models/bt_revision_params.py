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


class BTRevisionParams(object):
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
        'revision': 'str',
        'element_type': 'int',
        'element_id': 'str',
        'company_id': 'str',
        'part_number': 'str',
        'insertable_id': 'str',
        'release_id': 'str',
        'version_id': 'str',
        'document_id': 'str'
    }

    attribute_map = {
        'revision': 'revision',
        'element_type': 'elementType',
        'element_id': 'elementId',
        'company_id': 'companyId',
        'part_number': 'partNumber',
        'insertable_id': 'insertableId',
        'release_id': 'releaseId',
        'version_id': 'versionId',
        'document_id': 'documentId'
    }

    def __init__(self, revision=None, element_type=None, element_id=None, company_id=None, part_number=None, insertable_id=None, release_id=None, version_id=None, document_id=None):  # noqa: E501
        """BTRevisionParams - a model defined in OpenAPI"""  # noqa: E501

        self._revision = None
        self._element_type = None
        self._element_id = None
        self._company_id = None
        self._part_number = None
        self._insertable_id = None
        self._release_id = None
        self._version_id = None
        self._document_id = None
        self.discriminator = None

        if revision is not None:
            self.revision = revision
        if element_type is not None:
            self.element_type = element_type
        if element_id is not None:
            self.element_id = element_id
        if company_id is not None:
            self.company_id = company_id
        if part_number is not None:
            self.part_number = part_number
        if insertable_id is not None:
            self.insertable_id = insertable_id
        if release_id is not None:
            self.release_id = release_id
        if version_id is not None:
            self.version_id = version_id
        if document_id is not None:
            self.document_id = document_id

    @property
    def revision(self):
        """Gets the revision of this BTRevisionParams.  # noqa: E501


        :return: The revision of this BTRevisionParams.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this BTRevisionParams.


        :param revision: The revision of this BTRevisionParams.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def element_type(self):
        """Gets the element_type of this BTRevisionParams.  # noqa: E501


        :return: The element_type of this BTRevisionParams.  # noqa: E501
        :rtype: int
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this BTRevisionParams.


        :param element_type: The element_type of this BTRevisionParams.  # noqa: E501
        :type: int
        """

        self._element_type = element_type

    @property
    def element_id(self):
        """Gets the element_id of this BTRevisionParams.  # noqa: E501


        :return: The element_id of this BTRevisionParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTRevisionParams.


        :param element_id: The element_id of this BTRevisionParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def company_id(self):
        """Gets the company_id of this BTRevisionParams.  # noqa: E501


        :return: The company_id of this BTRevisionParams.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTRevisionParams.


        :param company_id: The company_id of this BTRevisionParams.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def part_number(self):
        """Gets the part_number of this BTRevisionParams.  # noqa: E501


        :return: The part_number of this BTRevisionParams.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTRevisionParams.


        :param part_number: The part_number of this BTRevisionParams.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def insertable_id(self):
        """Gets the insertable_id of this BTRevisionParams.  # noqa: E501


        :return: The insertable_id of this BTRevisionParams.  # noqa: E501
        :rtype: str
        """
        return self._insertable_id

    @insertable_id.setter
    def insertable_id(self, insertable_id):
        """Sets the insertable_id of this BTRevisionParams.


        :param insertable_id: The insertable_id of this BTRevisionParams.  # noqa: E501
        :type: str
        """

        self._insertable_id = insertable_id

    @property
    def release_id(self):
        """Gets the release_id of this BTRevisionParams.  # noqa: E501


        :return: The release_id of this BTRevisionParams.  # noqa: E501
        :rtype: str
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this BTRevisionParams.


        :param release_id: The release_id of this BTRevisionParams.  # noqa: E501
        :type: str
        """

        self._release_id = release_id

    @property
    def version_id(self):
        """Gets the version_id of this BTRevisionParams.  # noqa: E501


        :return: The version_id of this BTRevisionParams.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTRevisionParams.


        :param version_id: The version_id of this BTRevisionParams.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def document_id(self):
        """Gets the document_id of this BTRevisionParams.  # noqa: E501


        :return: The document_id of this BTRevisionParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTRevisionParams.


        :param document_id: The document_id of this BTRevisionParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

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
        if not isinstance(other, BTRevisionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
