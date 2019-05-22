"""
This file contains contents for Data Structures and Algorithms Revisited series
"""
import numpy as np
from classes import BigO
from classes import Plotter
from part4.linear_search import linear_search
from part4.binary_search import binary_search

def main():
    """
    Main function for this file
    Returns:

    """
    # Create BigO object and plotter for plotting
    binary_search_op = BigO('Binary Search')
    linear_search_op = BigO('Linear Search')
    plotter = Plotter()
    plotter.add_objects(binary_search_op, linear_search_op)

    for i in range(1000):
        # Create random array and random number to do binary search
        item_list = np.random.randint(0, i+1, size=i+1)
        item = np.random.randint(0, i+1)

        # Do the binary search
        binary_search_op.time_function(binary_search, item_list=item_list, item=item)
        linear_search_op.time_function(linear_search, item_list=item_list, item=item)

    plotter.to_plot()

if __name__ == '__main__':
    main()
