#!/usr/bin/env python3
'''
TestAccessNestedMap class that inherits from unittest.TestCase
'''
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    first test for utils.access_nested_map
    '''

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            result: Union[Mapping, int]):
        '''
        Test access nested map
        '''
        self.assertEqual(access_nested_map(nested_map, path), result)
