"""
Unittest file for binary search in part 4 post
"""

from unittest import TestCase
from part4.binary_search import binary_search

class TestBinarySearch(TestCase):
    """
    TestLinearSearch class overriding TestCase class
    """
    def test_binary_search(self):
        """
        Unittest for binary_search function in part4 directory. The return value should be the
        index of the number you are looking for. If such number doesn't exist, then -1 should be
        returned
        Returns:

        """
        # Check several function like this
        item_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(len(item_list)):
            self.assertEqual(i, binary_search(item_list, i))

        # Check if -1 will be returned in case of a number which doesn't exist in item_list
        self.assertEqual(-1, binary_search(item_list, -5))
        self.assertEqual(-1, binary_search(item_list, 99))
