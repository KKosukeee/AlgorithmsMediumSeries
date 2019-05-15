"""
Implement a queue class here using LinkedList class
"""
from classes import LinkedList

class Queue:
    """
    Queue class implementation
    """
    def __init__(self, node=None):
        """
        Initialization method for a queue object
        Args:
            node: Node object as the first element in the queue
        """
        # Create a linked-list object with FIFO structure
        self.list = LinkedList(node)

    def enqueue(self, node):
        """
        This method will add an element into the queue
        Args:
            node: Node object to add into the queue
        Returns:

        """
        # Append the element at the tail of the list
        self.list.append_right(node)

    def dequeue(self):
        """
        This method will get an element from the queue in FIFO manner
        Returns:

        """
        # Temporary get the head element
        head_element = self.list.head

        # Remove the head element
        self.list.remove(head_element)

        # Simply return the node object
        return head_element

    def peek(self):
        """
        This method will return an integer value of the first element
        Returns:

        """
        # Return the head element in the queue
        return self.list.head.value
