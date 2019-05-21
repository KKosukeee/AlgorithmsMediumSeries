"""
This file contains contents for Data Structures and Algorithms Revisited series
"""
import numpy as np
from classes import BigO
from classes import Plotter

def main():
    """
    Main function for this file
    Returns:

    """
    # Create BigO object and plotter for plotting
    binary_search_op = BigO('Binary Search')
    plotter = Plotter()
    plotter.add_object(binary_search_op)

    for i in range(1000):
        # Create random array and random number to do binary search
        item_list =  np.random.randint(0, i+1, size=i+1)
        item = np.random.randint(0, i+1)

        # Do the binary search
        binary_search_op.time_function(binary_search, item_list=item_list, item=item)

    plotter.to_plot()

def binary_search(item_list, item):
    """
    This function returns the index of item within item_list. If such item doesn't
    exist in item_list, -1 will be returned
    Args:
        item_list: list of integers where you look for item from
        item: int value that you are looking for from item_list
    Returns:
        int: index of the item within item_list. -1 will be returned if item doesn't exist
    """
    # Initialize left and right point for a binary search
    low, high = 0, len(item_list) - 1

    # Loop while low exceeds high (meaning element not found in the list)
    while low <= high:
        # Get middle pointer from low and high
        mid = (low + high) // 2

        # Now decide whether you look for left half or right half of the list
        if item_list[mid] < item:
            low = mid + 1
        elif item_list[mid] > item:
            high = mid - 1
        else:
            # Congrats! We found an element
            return mid

    return -1

if __name__ == '__main__':
    main()
