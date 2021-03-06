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


class BTVersionOrWorkspaceParams(object):
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
        'microversion_id': 'str',
        'read_only': 'bool',
        'is_release': 'bool',
        'from_history': 'bool',
        'workspace_id': 'str',
        'client_interaction_mode': 'str',
        'version_id': 'str',
        'document_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'microversion_id': 'microversionId',
        'read_only': 'readOnly',
        'is_release': 'isRelease',
        'from_history': 'fromHistory',
        'workspace_id': 'workspaceId',
        'client_interaction_mode': 'clientInteractionMode',
        'version_id': 'versionId',
        'document_id': 'documentId'
    }

    def __init__(self, name=None, description=None, microversion_id=None, read_only=None, is_release=None, from_history=None, workspace_id=None, client_interaction_mode=None, version_id=None, document_id=None):  # noqa: E501
        """BTVersionOrWorkspaceParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._description = None
        self._microversion_id = None
        self._read_only = None
        self._is_release = None
        self._from_history = None
        self._workspace_id = None
        self._client_interaction_mode = None
        self._version_id = None
        self._document_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if read_only is not None:
            self.read_only = read_only
        if is_release is not None:
            self.is_release = is_release
        if from_history is not None:
            self.from_history = from_history
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if client_interaction_mode is not None:
            self.client_interaction_mode = client_interaction_mode
        if version_id is not None:
            self.version_id = version_id
        if document_id is not None:
            self.document_id = document_id

    @property
    def name(self):
        """Gets the name of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The name of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTVersionOrWorkspaceParams.


        :param name: The name of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The description of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTVersionOrWorkspaceParams.


        :param description: The description of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The microversion_id of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTVersionOrWorkspaceParams.


        :param microversion_id: The microversion_id of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def read_only(self):
        """Gets the read_only of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The read_only of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this BTVersionOrWorkspaceParams.


        :param read_only: The read_only of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def is_release(self):
        """Gets the is_release of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The is_release of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_release

    @is_release.setter
    def is_release(self, is_release):
        """Sets the is_release of this BTVersionOrWorkspaceParams.


        :param is_release: The is_release of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: bool
        """

        self._is_release = is_release

    @property
    def from_history(self):
        """Gets the from_history of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The from_history of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: bool
        """
        return self._from_history

    @from_history.setter
    def from_history(self, from_history):
        """Sets the from_history of this BTVersionOrWorkspaceParams.


        :param from_history: The from_history of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: bool
        """

        self._from_history = from_history

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The workspace_id of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTVersionOrWorkspaceParams.


        :param workspace_id: The workspace_id of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def client_interaction_mode(self):
        """Gets the client_interaction_mode of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The client_interaction_mode of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: str
        """
        return self._client_interaction_mode

    @client_interaction_mode.setter
    def client_interaction_mode(self, client_interaction_mode):
        """Sets the client_interaction_mode of this BTVersionOrWorkspaceParams.


        :param client_interaction_mode: The client_interaction_mode of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: str
        """

        self._client_interaction_mode = client_interaction_mode

    @property
    def version_id(self):
        """Gets the version_id of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The version_id of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTVersionOrWorkspaceParams.


        :param version_id: The version_id of this BTVersionOrWorkspaceParams.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def document_id(self):
        """Gets the document_id of this BTVersionOrWorkspaceParams.  # noqa: E501


        :return: The document_id of this BTVersionOrWorkspaceParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTVersionOrWorkspaceParams.


        :param document_id: The document_id of this BTVersionOrWorkspaceParams.  # noqa: E501
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
        if not isinstance(other, BTVersionOrWorkspaceParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
