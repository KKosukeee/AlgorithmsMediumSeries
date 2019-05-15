"""
All the plot used in the "List-Based Collections: Queue" is created by this
file.
"""
import numpy as np
import matplotlib.pyplot as plt
from classes import Queue
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
    enqueue_op = BigO('Enqueue operation')
    dequeue_op = BigO('Dequeue operation')
    peek_op = BigO('Peek operation')

    # Add BigO objects to compare the plots
    plotter.add_objects(enqueue_op, dequeue_op, peek_op)

    for i in range(1000):
        queue = create_queue(i+1)

        # Time enqueue function with a queue where the size == i
        node = Node(np.random.randint(0, 1000))
        enqueue_op.time_function(enqueue_operation, node=node, queue=queue)

        # Time dequeue function with a dequeue where the size == 1
        dequeue_op.time_function(dequeue_operation, queue=queue)

        # Time peek function with a queue of size i.
        peek_op.time_function(peek_operaiton, queue=queue)

    plt.ylim((1e-7 - 1e-5, 1e-7 + 1e-5))
    plotter.to_plot()

def enqueue_operation(queue, node):
    """
    This function illustrate how enqueueing with a queue works, and plot its runtime
    complexity
    Args:
        queue: Queue object to enqueue an element with
        node: Node object to enqueue with
    Returns:

    """
    queue.enqueue(node)

def dequeue_operation(queue):
    """
    This function illustrate how dequeueing with a queue works, and plot its runtime
    complexity
    Args:
        queue: Queue object to dequeue an element from
    Returns:
        Node: an element popped out of queue by dequeue operation
    """
    return queue.dequeue()

def peek_operaiton(queue):
    """
    This function just peak an element from the queue. This is used to plot its runtime
    complexity
    Args:
        queue: Queue object to peak at with
    Returns:
        int: value of the top node in the queue
    """
    return queue.peek()

def create_queue(size):
    """
    This function create a queue object with the size specified as its input
    Args:
        size: int value representing the size of a queue
    Returns:
        Queue: Queue object with the length == size
    """
    # Initialize a queue
    queue = Queue()

    for _ in range(size):
        # Enqueue an element with random value into the queue
        queue.enqueue(Node(np.random.randint(0, 1000)))

    # Now return the queue
    return queue

if __name__ == '__main__':
    main()
