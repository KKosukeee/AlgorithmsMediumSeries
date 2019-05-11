"""
Unit test for Stack object
"""
from unittest import TestCase
from classes import Stack
from classes import Node

class TestStack(TestCase):
    """
    TestStack object implementation
    """
    def setUp(self):
        """
        Setup method for unit-testing. This method will be called for each test case
        in this file
        Returns:

        """
        # Create dummy nodes for testing the stack class
        self.first_node = Node(1)
        self.second_node = Node(2)
        self.third_node = Node(3)

        # Push all nodes into a stack
        self.stack = Stack()
        self.stack.push(self.first_node)
        self.stack.push(self.second_node)
        self.stack.push(self.third_node)

    def test_push(self):
        """
        Unit-test for stack.push method
        Returns:

        """
        # Add new element by pushing into the stack, then check the value
        new_element = Node(4)
        self.stack.push(new_element)
        self.assertEqual(new_element.value, self.stack.peek())

        # Add another element with push operation to make sure ;)
        new_element = Node(5)
        self.stack.push(new_element)
        self.assertEqual(new_element.value, self.stack.peek())

    def test_pop(self):
        """
        Unit-test for stack.pop method
        Returns:

        """
        # Pop an element one by one, then check the node
        self.assertEqual(self.stack.pop(), self.third_node)
        self.assertEqual(self.stack.pop(), self.second_node)
        self.assertEqual(self.stack.pop(), self.first_node)

    def test_peek(self):
        """
        Unit-test for stack.peek method
        Returns:

        """
        # Check if the nodes are properly stored into the stack
        self.assertEqual(self.third_node.value, self.stack.peek())
        new_element = Node(4)
        self.stack.push(new_element)
        self.assertEqual(new_element.value, self.stack.peek())

    def tearDown(self):
        """
        This method will be called at the end of unit-tests.
        Returns:

        """
