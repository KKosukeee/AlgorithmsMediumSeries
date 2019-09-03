"""
This file contains a content of part7 of the data structures and algorithms blog series.
"""
from classes import BigO
from classes import Plotter
import numpy as np
from part6.bubble_sort import bubble_sort
from part6.merge_sort import merge_sort
from part7.quick_sort import quick_sort

def main():
    """
    Main function of this file. It compares a couple of sorting algorithms that I created
    previous to the blog post.

    Returns:
        None:

    """
    # Create BigO instance for each sorting algorithm
    bubble_sort_op = BigO('Bubble Sort')
    merge_sort_op = BigO('Merge Sort')
    quick_sort_op = BigO('Quick Sort')
    plotter = Plotter()
    plotter.add_objects(bubble_sort_op, merge_sort_op, quick_sort_op)

    # Create an arbitrary array using numpy
    for i in range(1000):
        unsorted_array = np.random.randint(0, i+1, size=i+1)
        # Time function for each sorting algorithm
        bubble_sort_op.time_function(bubble_sort, array=unsorted_array.copy())
        merge_sort_op.time_function(merge_sort, array=unsorted_array.copy())
        quick_sort_op.time_function(quick_sort, array=unsorted_array.copy(), low=0, high=i)

    # Plot the comparisons
    plotter.to_plot()

if __name__ == '__main__':
    main()
