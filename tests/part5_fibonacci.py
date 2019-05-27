"""
This test contains a class for unit-testing the part5/recursions.py file
"""

from unittest import TestCase
from part5.recursions import fibonacci

class TestFibonacci(TestCase):
    """
    TestFibonacci class to test fibonacci function in part5/recursions.py file
    """
    def test_fibonacci(self):
        """
        This method will unit-test fibonacci function
        Returns:

        """
        answers = [1, 1, 2, 3, 5, 8, 13, 21]

        for i, answer in enumerate(answers):
            self.assertEqual(fibonacci(i), answer)
