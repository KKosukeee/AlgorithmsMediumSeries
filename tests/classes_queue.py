"""
Unit-test file for Queue object
"""
from unittest import TestCase
from classes import Queue
from classes import Node

class TestQueue(TestCase):
    """
    TestQueue object implementation
    """
    def setUp(self):
        """
        Setup method for unit-testing. This method will be called for each test case
        in this file
        Returns:

        """
        # Initialize a couple nodes to test the queue class
        self.first_node = Node(3)
        self.second_node = Node(2)
        self.third_node = Node(1)

        # Create a queue with elements created above
        self.queue = Queue()
        self.queue.enqueue(self.first_node)
        self.queue.enqueue(self.second_node)
        self.queue.enqueue(self.third_node)

    def test_enqueue(self):
        """
        Unit-test for queue.enqueue method which is supposed to add an element in the linked-list
        Returns:

        """
        # Enqueue a node into self.queue: 1->2->3->4
        new_node = Node(4)
        self.queue.enqueue(new_node)
        self.assertEqual(self.queue.peek(), self.first_node.value)

    def test_dequeue(self):
        """
        Unit-test for queue.dequeue method which is supposed to remove an element from the list in
        FIFO manner
        Returns:

        """
        # Dequeue a node from self.queue: 2->3
        self.assertEqual(self.queue.peek(), self.first_node.value)
        node = self.queue.dequeue()
        self.assertEqual(node.value, self.first_node.value)

        # Dequeue a node from self.queue: 3
        self.assertEqual(self.queue.peek(), self.second_node.value)
        node = self.queue.dequeue()
        self.assertEqual(node.value, self.second_node.value)

        # Dequeue the last element from self.queue: None
        self.assertEqual(self.queue.peek(), self.third_node.value)
        node = self.queue.dequeue()
        self.assertEqual(node.value, self.third_node.value)

    def test_peek(self):
        """
        Unit-test for queue.peek method which is supposed to get an element that will be
        the next element you get by calling enqueue method
        Returns:

        """
        # Check if its initially right
        self.assertEqual(self.first_node.value, self.queue.peek())
