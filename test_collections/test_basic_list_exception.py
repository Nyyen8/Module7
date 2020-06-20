"""
Program: test_basic_list_exception.py
Author: Paul Elsea
Last Modified: 06/20/2020

Program to test the make_list function using mocked get_input function output.
"""

import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as list

class TestList(unittest.TestCase):
    '''Test to pass mock input from get_input() into make_list to ensure value error is raised when non-numeric
    input is received.'''
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            list.make_list()

    '''Test to pass mock input from get_input() into make_list to ensure value error is raised when input below 1
    is received.'''
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='-2')
    def test_make_list_below_1(self, input):
        with self.assertRaises(ValueError):
            list.make_list()

    '''Test to pass mock input from get_input() into make_list to ensure value error is raised when input above 50
    is received.'''
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='55')
    def test_make_list_above_50(self, input):
        with self.assertRaises(ValueError):
            list.make_list()


if __name__ == '__main__':
    unittest.main()
