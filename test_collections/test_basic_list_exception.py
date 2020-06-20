"""
Program: test_basic_list.py
Author: Paul Elsea
Last Modified: 06/19/2020

Program to test the make_list function using mocked get_input function output.
"""

import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as list

'''Test to pass input mock input from get_input() into make_list to ensure correct list is returned.'''
class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            list.make_list()


if __name__ == '__main__':
    unittest.main()
