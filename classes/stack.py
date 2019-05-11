"""
Stack implementation
"""
from classes import LinkedList

class Stack:
    """
    Stack class implementation
    """
    def __init__(self, top=None):
        """
        Create a stack by calling this initialization method
        Args:
            top: Node class default to None. This will be the first element in the stack
        """
        # Stack can be implemented with linked-lists as well :D
        self.list = LinkedList(top)

    def push(self, node):
        """
        This operation adds a node into a stack
        Args:
            node: Node class. The node is added on top of the stack in LIFO manner
        Returns:

        """
        # This will add an element at the head of the linked-list
        self.list.insert(node, 1)

    def pop(self):
        """
        This operation will get an element from a stack in LIFO manner
        Returns:
            Node: top node object within the stack.
        """
        # Temporary get the top element
        top_element = self.list.head

        # Now remove the reference to the next node by calling remove method
        self.list.remove(top_element)

        # Simply return the top element
        return top_element

    def peek(self):
        """
        You can look up the top element in O(1) time with this method without popping it out
        Returns:
            int: integer value for the top element in the stack
        """
        # Return integer value of the top element
        return self.list.head.value
