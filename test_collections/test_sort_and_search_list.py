"""
Program: test_sort_and_search_list.py
Author: Paul Elsea
Last Modified: 06/20/2020

Program to test sort and search list functions from sort_and_search_list.py.
"""

import unittest
from fun_with_collections import sort_and_search_list as SandS


class List_Test_Cases(unittest.TestCase):
    '''Test to make sure search_list returns correct index position.'''
    def test_search_found(self):
        self.assertEqual(SandS.search_list('dog'), 0)

    '''Test to make sure search_list returns -1 if item not present in list.'''
    def test_search_not_found(self):
        self.assertEqual(SandS.search_list('pangolin'), -1)

    '''Test to make sure sort_list returns correctly sorted list.'''
    def test_something(self):
        self.assertEqual(SandS.sort_list(), ['cat', 'dog', 'mouse'])


if __name__ == '__main__':
    unittest.main()
