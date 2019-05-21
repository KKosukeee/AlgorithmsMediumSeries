"""
This file contains contents for Data Structures and Algorithms Revisited series
"""
import numpy as np
from classes import BigO
from classes import Plotter

def main():
    """
    Main function to this file
    Returns:

    """
    # Create BigO and Plotter object
    linear_search_op = BigO('Linear Search')
    plotter = Plotter()
    plotter.add_object(linear_search_op)

    # Create arrays with random elements in it
    for i in range(1000):
        # Create random array and random number to do binary search
        item_list = np.random.randint(0, i + 1, size=i + 1)
        item = np.random.randint(0, i + 1)

        # Do the binary search
        linear_search_op.time_function(linear_search, item_list=item_list, item=item)

    plotter.to_plot()

def linear_search(item_list, item):
    """
    This function does the linear search on item_list argument. the index of item within item_list
    will be returned if found, otherwise -1 will be returned by this function
    Args:
        item_list: list of integers where you look for item
        item: int value that you are looking for from item_list
    Returns:
        int: index of the item within the item_list. If no item exists in the item_list, -1 will
            be returned
    """
    for i in range(len(item_list)):
        if item_list[i] == item:
            return i

    return -1

if __name__ == '__main__':
    main()
