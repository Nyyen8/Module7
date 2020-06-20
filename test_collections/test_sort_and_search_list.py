"""
Program: test_sort_and_search_list.py
Author: Paul Elsea
Last Modified: 06/20/2020

Program to test sort and search list functions from sort_and_search_list.py.
"""

import unittest
from fun_with_collections import sort_and_search_list as SandS


class List_Test_Cases(unittest.TestCase):
    def test_search_found(self):
        self.assertEqual(SandS.search_list('dog'), 1)

    def test_search_not_found(self):
        self.assertEqual(SandS.search_list('pangolin'), -1)

    def test_something(self):
        animal_list = ['mouse', 'cat', 'dog']
        self.assertEqual(SandS.sort_list(animal_list), ['dog', 'cat', 'mouse'])


if __name__ == '__main__':
    unittest.main()
