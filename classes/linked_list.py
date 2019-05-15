"""
An implementation for linked-list
"""

class LinkedList:
    """
    LinkedList class implementation
    """
    def __init__(self, head=None):
        """
        Head node of a new linked-list object
        Args:
            head: Node class. This node will be a head of the linked-list
        """
        self.head = head
        self.tail = head

    def append_right(self, node):
        """
        This method will add a new element to the end of the linked-list
        Args:
            node: Node object to append the end of the linked-list
        Returns:
        """
        # If the head or the tail is None, then it must be an empty list
        if not self.tail or not self.head:
            self.head = node
            self.tail = node
        # Otherwise, simply append to its tail which takes O(1)
        else:
            self.tail.next = node
            self.tail = node

    def append_left(self, node):
        """
        This method will add a new element at the head of the list.
        After this operation, input node is going to be the new head.
        Args:
            node: Node object to set as the new head.
        Returns:
        """
        # Set input node's next as the previous head
        node.next = self.head

        # Then new head is set to the input node :D
        self.head = node

    def remove(self, node):
        """
        Removes a node from the linked-list
        Args:
            node: Node object to remove from the list
        Returns:
        """
        # Check if removing the head or not
        if self.head == node:
            # Update head value as the input node
            self.head = self.head.next

            # If self.head is None, then it means the list empty
            if not self.head:
                self.tail = None
        else:
            current = self.head

            # Loop until current node is previous to the input node
            while current and current.next != node:
                current = current.next

            # Update self.tail if the current.next is the one
            if self.tail == node:
                self.tail = current

            current.next = node.next

    def insert(self, node, position):
        """
        Inserts a node with specified position (index)
        Args:
            node: Node object to insert at specified position
            position: integer value with range 0 < position <= len(list)
        Returns:
        """
        # Placeholder for current and previous nodes
        current = self.head
        previous = None

        for _ in range(position - 1):
            previous = current
            current = current.next

        # Assign previous.next with inserting node
        if previous:
            previous.next = node
        # If previous is None, then new node should be the head
        else:
            self.head = node

        # Assign new node's next to the current node
        node.next = current

        # If current is None, then it means we are appending a node
        if not current:
            self.tail = node

    def search(self, value):
        """
        Searches a value in the linked-list.
        It will raise an error if the value is not found
        Args:
            value: integer value to search for
        Returns:
            Node: will return first Node with value == value
        """
        current = self.head

        while current and current.value != value:
            current = current.next

        return current

    def lookup(self, position):
        """
        Does the similar thing with indexing an array
        Args:
            position: position to lookup a value in a linked-list
        Returns:
            int: returns a value for nth node where n is specified with position argument
        """
        # Initialize counter as 1 because position starts from 1 to n
        current = self.head
        counter = 1

        # Loop through the list until we reach to the position
        while counter < position:
            current = current.next
            counter += 1

        return current.value
