# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class StatisticEntry(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_property': 'str',
        'entities': 'list[StatisticEntity]'
    }

    attribute_map = {
        '_property': 'property',
        'entities': 'entities'
    }

    def __init__(self, _property=None, entities=None):  # noqa: E501
        """StatisticEntry - a model defined in Swagger"""  # noqa: E501
        self.__property = None
        self._entities = None
        self.discriminator = None
        self._property = _property
        self.entities = entities

    @property
    def _property(self):
        """Gets the _property of this StatisticEntry.  # noqa: E501


        :return: The _property of this StatisticEntry.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this StatisticEntry.


        :param _property: The _property of this StatisticEntry.  # noqa: E501
        :type: str
        """
        if _property is None:
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501

        self.__property = _property

    @property
    def entities(self):
        """Gets the entities of this StatisticEntry.  # noqa: E501


        :return: The entities of this StatisticEntry.  # noqa: E501
        :rtype: list[StatisticEntity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this StatisticEntry.


        :param entities: The entities of this StatisticEntry.  # noqa: E501
        :type: list[StatisticEntity]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")  # noqa: E501

        self._entities = entities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(StatisticEntry, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatisticEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
