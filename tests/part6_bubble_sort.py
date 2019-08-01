"""
Unittest file for bubble sort function in part6 post
"""

from unittest import TestCase
from part6.bubble_sort import bubble_sort
import numpy as np

class TestBubbleSort(TestCase):
    """
    TestBubbleSort object implementation which overrides TestCase object
    """
    def test_bubble_sort(self):
        """
        Unittest for bubble_sort function in part 6 directory. The return value should be sorted
        array, while the input array is an unsorted array. If the returned array isn't sorted, the
        test fails
        Returns:

        """
        # Test bubble_sort function N times
        for _ in range(10):

            # Create an unsorted array
            unsorted_array = np.random.randint(0, 100, size=np.random.randint(100))

            # Compare the sorted array from bubble_sort function and the numpy function
            sorted_array = bubble_sort(unsorted_array.copy())
            unsorted_array.sort()
            self.assertTrue(np.all(sorted_array == unsorted_array))
