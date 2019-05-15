"""
Unit test file for LinkedList class
"""
from unittest import TestCase
from classes import Node
from classes import LinkedList

class TestLinkedList(TestCase):
    """
    Unit test implementation for LinkedList class
    """
    def setUp(self):
        """
        Setup method to initialize a linked-list
        Returns:

        """
        # Create test nodes
        self.head_node = Node(1)
        self.second_node = Node(2)
        self.third_node = Node(3)

        # Create test linked-list
        self.list = LinkedList(self.head_node)

        # Append nodes such that the list is: 1->2->3
        self.list.append_right(self.second_node)
        self.list.append_right(self.third_node)

    def test_append_right(self):
        """
        Unit-test for append method in LinkedList class
        Returns:

        """
        # Append new node with value of 4 such that: 1->2->3->4
        current = self.list.head
        new_node = Node(4)
        self.list.append_right(new_node)

        # Check if all values are the same as 1 to 4
        for i in range(1, 5):
            self.assertEqual(current.value, i)
            current = current.next

        # Check if the tail element is the new_node
        self.assertEqual(new_node.value, self.list.tail.value)

    def test_append_left(self):
        """
        Unit-test for appending an element as the new head of the
        linked-list
        Returns:

        """
        # Create potential head node
        new_node = Node(0)

        # Then call the function to set it as the head node
        self.list.append_left(new_node)

        # Create current node to traverse
        current = self.list.head

        # Traverse the list, then check the values
        for i in range(4):
            self.assertEqual(current.value, i)
            current = current.next

    def test_insert(self):
        """
        Unit-test for insert method in LinkedList class
        Returns:

        """
        # Insert node as the new head: 0->1->2->3
        new_node = Node(0)
        self.list.insert(new_node, 1)

        # Check if correctly inserted or not
        self.assertEqual(self.list.head.value, new_node.value)
        self.assertEqual(self.list.tail.value, self.third_node.value)

        # Insert in the middle of the list: 0->1->5->2->3
        new_node = Node(5)
        self.list.insert(new_node, 3)

        # Check if correctly inserted or not
        self.assertEqual(self.list.head.next.next.value, new_node.value)

        # Insert node as the tail of the list: 0->1->5->2->3->9
        new_node = Node(9)
        self.list.insert(new_node, 6)

        # Check if correctly inserted or not
        self.assertEqual(self.list.tail.value, new_node.value)

        # Get temporary access to the list's head
        current = self.list.head

        # Get the tail node from the list
        while current.next:
            current = current.next

        # Check if correctly inserted or not
        self.assertEqual(current.value, new_node.value)
        self.assertEqual(current.value, self.list.tail.value)

    def test_search(self):
        """
        Unit-test for search method in LinkedList class
        Returns:

        """
        # Check for the head node
        head_node = self.list.search(1)
        self.assertEqual(head_node, self.head_node)

        # Check for the second node
        second_node = self.list.search(2)
        self.assertEqual(second_node, self.second_node)

        # Check for the third node
        third_node = self.list.search(3)
        self.assertEqual(third_node, self.third_node)

    def test_remove(self):
        """
        Unit-test for remove method in LinkedList class
        Returns:

        """
        # Remove the first node in the list: 2->3
        self.list.remove(self.head_node)
        current = self.list.head

        # Check for all nodes which range from 2 to 3
        for i in range(2, 4):
            self.assertEqual(current.value, i)
            current = current.next

        # Check is list's head is updated properly
        self.assertEqual(self.list.head, self.second_node)
        self.assertEqual(self.list.tail, self.third_node)

        # Remove the second node in the list: 3
        self.list.remove(self.second_node)
        self.assertEqual(self.list.head.value, self.third_node.value)
        self.assertEqual(self.list.tail, self.third_node)

        # Remove the third node in the list, so the head should be None
        self.list.remove(self.third_node)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_lookup(self):
        """
        Unit-test for lookup operation in LinkedList object
        Returns:

        """
        for i in range(1, 4):
            self.assertEqual(self.list.lookup(i), i)

    def tearDown(self):
        """
        Remove any files created by the unit-test
        Returns:

        """
