"""
Unittest file for linear search in part 4 post
"""

from unittest import TestCase
from part4.linear_search import linear_search

class TestBinarySearch(TestCase):
    """
    TestBinarySearch class overriding TestCase class
    """
    def test_binary_search(self):
        """
        Unittest for linear_search function in part4 directory.
        Returns:

        """
        # Check several function like this
        item_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(len(item_list)):
            self.assertEqual(i, linear_search(item_list, i))

        # Check if -1 will be returned in case of a number which doesn't exist in item_list
        self.assertEqual(-1, linear_search(item_list, -5))
        self.assertEqual(-1, linear_search(item_list, 99))
