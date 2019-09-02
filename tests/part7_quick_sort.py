"""
A unit-test file for quick sort function in part7 of the blog post
"""
from unittest import TestCase
from part7.quick_sort import quick_sort
import numpy as np

class TestQuickSort(TestCase):
    """
    This class tests part7.quick_sort.quick_sort function which is supposed to sort an array
    using quick sort algorithm
    """
    def test_quick_sort(self):
        """
        Unit-test for quick_sort function in part7 directory. It tests with 10 test cases with
        randomly generated array using numpy function. The result should match with the sorted array
        via numpy function.

        Returns:
            None:

        """
        # Test quick_sort function 10 times
        for _ in range(10):
            # Create an arbitrary array using numpy randint function
            unsorted_array = np.random.randint(0, 100, size=np.random.randint(100))
            copied_array = unsorted_array.copy()

            # Call quick sort and compare with the sorted array via numpy function
            quick_sort(unsorted_array, 0, unsorted_array.size-1)
            np.testing.assert_array_equal(np.sort(copied_array), unsorted_array)
