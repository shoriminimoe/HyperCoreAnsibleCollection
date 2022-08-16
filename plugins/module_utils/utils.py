# -*- coding: utf-8 -*-
# Copyright: (c) 2022, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod

__metaclass__ = type

import uuid

from ..module_utils.errors import InvalidUuidFormatError


def validate_uuid(value):
    try:
        uuid.UUID(value, version=4)
    except ValueError:
        raise InvalidUuidFormatError(value)


def filter_dict(input, *field_names):
    output = {}
    for field_name in field_names:
        if field_name not in input:
            continue
        value = input[field_name]
        if value is not None:
            output[field_name] = value
    return output


def transform_ansible_to_hypercore_query(ansible_query, ansible_hypercore_map):
    """
    Renames columns. Usually used to rename from ansible-native to hypercore-native input
    :param ansible_query: keys as columns the way they're named in ansible and values of those columns as its values
    :param ansible_hypercore_map: keys as column names in ansible-native and values as names
     of those columns in hypercore
    :return: hypercore query
    """
    return {
        ansible_hypercore_map[key]: ansible_query[key]
        for key, value in ansible_query.items()
    }


class PayloadMapper:

    """
    Represent abstract class from which each 'endpoint class' will inherit from.
    Every class that will represent module object will (most likely) have to implement those methods.
    """

    @abstractmethod
    def to_ansible(self):
        """
        Transforms from python-native to ansible-native object.
        Used mostly in *_info modules for performing GET requests
        :return: ansible-native dictionary.
        """
        pass

    @abstractmethod
    def to_hypercore(self):
        """
        Transforms python-native to hypercore-native object.
        Used for using either post or patch methods onto hypercore API.
        :return: hypercore-native dictionary.
        """
        pass

    @classmethod
    @abstractmethod
    def from_ansible(cls, ansible_data):
        """
        Transforms from ansible_data (module.params) to python-object.
        :param ansible_data: Field that is inputed from ansible playbook. Is most likely
        equivalent to "module.params" in python
        :return: python object
        """
        pass

    @classmethod
    @abstractmethod
    def from_hypercore(cls, hypercore_data):
        """
        Transforms from hypercore-native dictionary to python-object.
        :param hypercore_data: Dictionary from hypercore API
        :return: python object
        """
        pass

    def __str__(self):
        return str(dict(ansible=self.to_ansible(), hypercore=self.to_hypercore()))
