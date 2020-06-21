"""
Program: test_sort_and_search_array.py
Author: Paul Elsea
Last Modified: 06/21/2020

Program to test sort and search array functions from sort_and_search_array.py.
"""

import unittest
import array as arr
from unittest.mock import patch
from fun_with_collections import sort_and_search_array as SSarray

class Array_Test_Case(unittest.TestCase):

    '''Test to make sure build_array makes the expected array.'''
    @patch('fun_with_collections.sort_and_search_array.get_input', return_value='7')
    def test_build_array(self, input):
        self.assertEqual(SSarray.build_array(), arr.array('i', [7, 7, 7]))

    '''Test to make sure search_array returns correct index position.'''
    def test_search_found(self):
        test_array = arr.array('i', [1, 3, 5, 7, 9, 0, 2, 4, 6, 8])
        self.assertEqual(SSarray.search_array(test_array, 7), 3)

    '''Test to make sure search_array returns -1 if item not present in array.'''
    def test_search_not_found(self):
        test_array = arr.array('i', [1, 3, 5, 7, 9, 0, 2, 4, 6, 8])
        self.assertEqual(SSarray.search_array(test_array, 'pangolin'), -1)

    '''Test to make sure sort_list returns correctly sorted array.'''
    def test_sort_array(self):
        test_array = arr.array('i', [1, 3, 5, 7, 9, 0, 2, 4, 6, 8])
        self.assertEqual(SSarray.sort_array(test_array), arr.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))



if __name__ == '__main__':
    unittest.main()
