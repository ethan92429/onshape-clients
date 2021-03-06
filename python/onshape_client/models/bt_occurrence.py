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


class BTOccurrence(object):
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
        'root_occurrence': 'bool',
        'full_path_as_string': 'str',
        'tail_instance_id': 'str',
        'head_instance_id': 'str',
        'occurrence_without_head': 'BTOccurrence',
        'occurrence_without_tail': 'BTOccurrence',
        'path': 'list[str]',
        'type_id': 'int',
        'connection_source': 'BTConnection',
        'export_type_name': 'str',
        'unknown_class': 'bool'
    }

    attribute_map = {
        'root_occurrence': 'rootOccurrence',
        'full_path_as_string': 'fullPathAsString',
        'tail_instance_id': 'tailInstanceId',
        'head_instance_id': 'headInstanceId',
        'occurrence_without_head': 'occurrenceWithoutHead',
        'occurrence_without_tail': 'occurrenceWithoutTail',
        'path': 'path',
        'type_id': 'typeId',
        'connection_source': 'connectionSource',
        'export_type_name': 'exportTypeName',
        'unknown_class': 'unknownClass'
    }

    def __init__(self, root_occurrence=None, full_path_as_string=None, tail_instance_id=None, head_instance_id=None, occurrence_without_head=None, occurrence_without_tail=None, path=None, type_id=None, connection_source=None, export_type_name=None, unknown_class=None):  # noqa: E501
        """BTOccurrence - a model defined in OpenAPI"""  # noqa: E501

        self._root_occurrence = None
        self._full_path_as_string = None
        self._tail_instance_id = None
        self._head_instance_id = None
        self._occurrence_without_head = None
        self._occurrence_without_tail = None
        self._path = None
        self._type_id = None
        self._connection_source = None
        self._export_type_name = None
        self._unknown_class = None
        self.discriminator = None

        if root_occurrence is not None:
            self.root_occurrence = root_occurrence
        if full_path_as_string is not None:
            self.full_path_as_string = full_path_as_string
        if tail_instance_id is not None:
            self.tail_instance_id = tail_instance_id
        if head_instance_id is not None:
            self.head_instance_id = head_instance_id
        if occurrence_without_head is not None:
            self.occurrence_without_head = occurrence_without_head
        if occurrence_without_tail is not None:
            self.occurrence_without_tail = occurrence_without_tail
        if path is not None:
            self.path = path
        if type_id is not None:
            self.type_id = type_id
        if connection_source is not None:
            self.connection_source = connection_source
        if export_type_name is not None:
            self.export_type_name = export_type_name
        if unknown_class is not None:
            self.unknown_class = unknown_class

    @property
    def root_occurrence(self):
        """Gets the root_occurrence of this BTOccurrence.  # noqa: E501


        :return: The root_occurrence of this BTOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._root_occurrence

    @root_occurrence.setter
    def root_occurrence(self, root_occurrence):
        """Sets the root_occurrence of this BTOccurrence.


        :param root_occurrence: The root_occurrence of this BTOccurrence.  # noqa: E501
        :type: bool
        """

        self._root_occurrence = root_occurrence

    @property
    def full_path_as_string(self):
        """Gets the full_path_as_string of this BTOccurrence.  # noqa: E501


        :return: The full_path_as_string of this BTOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._full_path_as_string

    @full_path_as_string.setter
    def full_path_as_string(self, full_path_as_string):
        """Sets the full_path_as_string of this BTOccurrence.


        :param full_path_as_string: The full_path_as_string of this BTOccurrence.  # noqa: E501
        :type: str
        """

        self._full_path_as_string = full_path_as_string

    @property
    def tail_instance_id(self):
        """Gets the tail_instance_id of this BTOccurrence.  # noqa: E501


        :return: The tail_instance_id of this BTOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._tail_instance_id

    @tail_instance_id.setter
    def tail_instance_id(self, tail_instance_id):
        """Sets the tail_instance_id of this BTOccurrence.


        :param tail_instance_id: The tail_instance_id of this BTOccurrence.  # noqa: E501
        :type: str
        """

        self._tail_instance_id = tail_instance_id

    @property
    def head_instance_id(self):
        """Gets the head_instance_id of this BTOccurrence.  # noqa: E501


        :return: The head_instance_id of this BTOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._head_instance_id

    @head_instance_id.setter
    def head_instance_id(self, head_instance_id):
        """Sets the head_instance_id of this BTOccurrence.


        :param head_instance_id: The head_instance_id of this BTOccurrence.  # noqa: E501
        :type: str
        """

        self._head_instance_id = head_instance_id

    @property
    def occurrence_without_head(self):
        """Gets the occurrence_without_head of this BTOccurrence.  # noqa: E501


        :return: The occurrence_without_head of this BTOccurrence.  # noqa: E501
        :rtype: BTOccurrence
        """
        return self._occurrence_without_head

    @occurrence_without_head.setter
    def occurrence_without_head(self, occurrence_without_head):
        """Sets the occurrence_without_head of this BTOccurrence.


        :param occurrence_without_head: The occurrence_without_head of this BTOccurrence.  # noqa: E501
        :type: BTOccurrence
        """

        self._occurrence_without_head = occurrence_without_head

    @property
    def occurrence_without_tail(self):
        """Gets the occurrence_without_tail of this BTOccurrence.  # noqa: E501


        :return: The occurrence_without_tail of this BTOccurrence.  # noqa: E501
        :rtype: BTOccurrence
        """
        return self._occurrence_without_tail

    @occurrence_without_tail.setter
    def occurrence_without_tail(self, occurrence_without_tail):
        """Sets the occurrence_without_tail of this BTOccurrence.


        :param occurrence_without_tail: The occurrence_without_tail of this BTOccurrence.  # noqa: E501
        :type: BTOccurrence
        """

        self._occurrence_without_tail = occurrence_without_tail

    @property
    def path(self):
        """Gets the path of this BTOccurrence.  # noqa: E501


        :return: The path of this BTOccurrence.  # noqa: E501
        :rtype: list[str]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BTOccurrence.


        :param path: The path of this BTOccurrence.  # noqa: E501
        :type: list[str]
        """

        self._path = path

    @property
    def type_id(self):
        """Gets the type_id of this BTOccurrence.  # noqa: E501


        :return: The type_id of this BTOccurrence.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this BTOccurrence.


        :param type_id: The type_id of this BTOccurrence.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def connection_source(self):
        """Gets the connection_source of this BTOccurrence.  # noqa: E501


        :return: The connection_source of this BTOccurrence.  # noqa: E501
        :rtype: BTConnection
        """
        return self._connection_source

    @connection_source.setter
    def connection_source(self, connection_source):
        """Sets the connection_source of this BTOccurrence.


        :param connection_source: The connection_source of this BTOccurrence.  # noqa: E501
        :type: BTConnection
        """

        self._connection_source = connection_source

    @property
    def export_type_name(self):
        """Gets the export_type_name of this BTOccurrence.  # noqa: E501


        :return: The export_type_name of this BTOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._export_type_name

    @export_type_name.setter
    def export_type_name(self, export_type_name):
        """Sets the export_type_name of this BTOccurrence.


        :param export_type_name: The export_type_name of this BTOccurrence.  # noqa: E501
        :type: str
        """

        self._export_type_name = export_type_name

    @property
    def unknown_class(self):
        """Gets the unknown_class of this BTOccurrence.  # noqa: E501


        :return: The unknown_class of this BTOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_class

    @unknown_class.setter
    def unknown_class(self, unknown_class):
        """Sets the unknown_class of this BTOccurrence.


        :param unknown_class: The unknown_class of this BTOccurrence.  # noqa: E501
        :type: bool
        """

        self._unknown_class = unknown_class

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
        if not isinstance(other, BTOccurrence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
