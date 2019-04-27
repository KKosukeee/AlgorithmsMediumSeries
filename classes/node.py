"""
An implementation of node for a linked-list
"""

class Node:
    """
    Node class implementation
    """
    def __init__(self, value):
        """
        A value for this particular node
        Args:
            value: integer
        """
        self.value = value
        self.next = None
