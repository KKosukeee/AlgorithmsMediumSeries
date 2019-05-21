"""
Unit-test for functions within part1_what_are_algorithms.py file
"""

from unittest import TestCase
from part1.what_are_algorithms import naive_approach
from part1.what_are_algorithms import optimal_approach

class TestWhatAreAlgorithms(TestCase):
    """
    Test case for both naive and optimal approach
    """
    def setUp(self):
        self.cases = (
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 1, 4, 11], 14, [0, 3]),
            ([5, 1, 9, 2], 12, []),
        )

    def test_naive_approach(self):
        """
        Tests two sum problem with naive function
        Returns:

        """
        for nums, target, answer in self.cases:
            self.assertListEqual(naive_approach(nums, target), answer)

    def test_optimal_approach(self):
        """
        Tests two-sum problem with optimal function
        Returns:

        """
        for nums, target, answer in self.cases:
            self.assertListEqual(optimal_approach(nums, target), answer)
