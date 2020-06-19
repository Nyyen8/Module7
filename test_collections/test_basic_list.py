"""
Program: test_basic_list.py
Author: Paul Elsea
Last Modified: 06/19/2020

Program to test the make_list function using mocked get_input function output.
"""

import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as list

'''Test to pass input mock input from get_input() into make_list to ensure correct list is returned.'''
class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value = '7')
    def test_make_list(self, input):
        self.assertEqual(list.make_list(), [7, 7, 7])


if __name__ == '__main__':
    unittest.main()
