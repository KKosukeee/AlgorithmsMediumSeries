"""
This test contains a class for unit-testing the part5/dps.py file
"""

from unittest import TestCase
from part5.dps import fibonacci

class TestDPs(TestCase):
    """
    TestFibonacci class to test fibonacci function in part5/dps.py file
    """
    def test_fibonacci(self):
        """
        This method will unit-test fibonacci function
        Returns:

        """
        answers = [1, 1, 2, 3, 5, 8, 13, 21]

        for i, answer in enumerate(answers):
            self.assertEqual(fibonacci(i, {}), answer)
