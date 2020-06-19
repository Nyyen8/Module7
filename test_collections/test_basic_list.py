"""
Program: test_basic_list.py
Author: Paul Elsea
Last Modified: 06/19/2020

Program to
"""

import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value = '7')
    def test_make_list(self):
        self.assertEqual(list.make_list(), [7, 7, 7])


if __name__ == '__main__':
    unittest.main()
