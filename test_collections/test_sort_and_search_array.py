"""
Program: test_sort_and_search_array.py
Author: Paul Elsea
Last Modified: 06/21/2020

Program to test sort and search array functions from sort_and_search_array.py.
"""

import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_array as SSarray

class Array_Test_Case(unittest.TestCase):

    '''Test to make sure build_array makes the expected array.'''
    @patch('fun_with_collections.sort_and_search_array.get_input', return_value='7')
    def test_build_array(self, input):
        self.assertEqual(SSarray.build_array(), [7, 7, 7])

    '''Test to make sure search_list returns correct index position.'''
    def test_search_found(self, input):
        test_array =
        self.assertEqual(SSarray.search_array(7), 0)

    '''Test to make sure search_list returns -1 if item not present in list.'''
    def test_search_not_found(self, input):
        self.assertEqual(SSarray.search_array('pangolin'), -1)

    '''Test to make sure sort_list returns correctly sorted list.'''
    def test_sort_array(self, input):
        self.assertEqual(SSarray.sort_array(), ['cat', 'dog', 'mouse'])



if __name__ == '__main__':
    unittest.main()
