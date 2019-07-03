"""
Unittest file for merge sort function in part 6 directory
"""

from unittest import TestCase
import numpy as np
from part6.merge_sort import merge_sort

class TestMergeSort(TestCase):
    """
    TestMergeSort class implementation by overriding the TestCase class
    """
    def test_merge_sort(self):
        """
        Unittest for merge_sort function in part6 directory. The return value
        should be a sorted array, while the input array isn't sorted. If the return
        array isn't sorted, then it's going to raise an error
        Returns:

        """
        # Test merge_sort function N times
        for _ in range(10):

            # Create an unsorted array with np.random function
            unsorted_array = np.random.randint(0, 100, size=np.random.randint(100))

            # Now sort the array with merge_sort function
            sorted_array = merge_sort(unsorted_array.copy())
            unsorted_array.sort()

            # Now compare if they are the same or not
            self.assertTrue(np.all(sorted_array == unsorted_array))
