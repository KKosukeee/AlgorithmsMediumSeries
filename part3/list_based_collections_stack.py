"""
All the plot used in the "List-Based Collections: Stack" is created by this
file.
"""
import numpy as np
import matplotlib.pyplot as plt
from classes import Stack
from classes import Node
from classes import BigO
from classes import Plotter

def main():
    """
    Main function for this file
    Returns:

    """
    # Initialize a plotter
    plotter = Plotter()

    # Create BigO object to observe for each runtime complexity
    push_op = BigO('Push operation')
    pop_op = BigO('Pop operation')
    peek_op = BigO('Peek operation')

    # Add BigO objects to compare the plots
    plotter.add_objects(push_op, pop_op, peek_op)

    for i in range(1000):
        stack = create_stack(i+1)

        # Time push function with a stack where the size == i
        node = Node(np.random.randint(0, 1000))
        push_op.time_function(push_operation, node=node, stack=stack)

        # Time pop function with a stack where the size == 1
        pop_op.time_function(pop_operation, stack=stack)

        # Time peek function with a stack of size i.
        peek_op.time_function(peek_operaiton, stack=stack)

    plt.ylim((1e-7 - 1e-5, 1e-7 + 1e-5))
    plotter.to_plot()

def push_operation(stack, node):
    """
    This function illustrate how pushing with a stack works, and plot its runtime
    complexity
    Args:
        stack: Stack object to push an element to
        node: Node object to push with
    Returns:

    """
    stack.push(node)

def pop_operation(stack):
    """
    This function illustrate how popping with a stack works, and plot its runtime
    complexity
    Args:
        stack: Stack object to pop an element from
    Returns:
        Node: an element popped out of stack by pop operation
    """
    return stack.pop()

def peek_operaiton(stack):
    """
    This function just peak an element from the stack. This is used to plot its runtime
    complexity
    Args:
        stack: Stack object to peak at with
    Returns:
        int: value of the top node in the stack
    """
    return stack.peek()

def create_stack(size):
    """
    This function create a stack object with the size specified as its input
    Args:
        size: int value representing the size of a stack
    Returns:
        Stack: Stack object with the length == size
    """
    # Initialize a stack
    stack = Stack()

    for _ in range(size):
        # Push an element with random value into the stack
        stack.push(Node(np.random.randint(0, 1000)))

    # Now return the stack
    return stack

if __name__ == '__main__':
    main()
