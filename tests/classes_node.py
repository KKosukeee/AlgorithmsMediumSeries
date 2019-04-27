"""
Unit-test for Node class
"""

from unittest import TestCase
from classes import Node

class TestNode(TestCase):
    """
    Test case for Node object
    """
    def setUp(self):
        """
        Setup method for initializing nodes
        Returns:

        """
        self.first_node = Node(1)
        self.second_node = Node(2)
        self.first_node.next = self.second_node

    def test_properties(self):
        """
        Unit-test for Node's properties
        Returns:

        """
        # Check for node's value property
        self.assertEqual(self.first_node.value, 1)
        self.assertEqual(self.second_node.value, 2)

        # Check for node's next property
        self.assertEqual(self.first_node.next, self.second_node)

    def tearDown(self):
        """
        Remove any files created for the unit-test
        Returns:

        """
