"""
Bubble sort implementation for part 6 of the Data Structures and Algorithms
"""
import numpy as np
from classes import BigO
from classes import Plotter

def main():
    """
    Main function of this file
    Returns:

    """
    # Create BigO object for measuring the performance
    bubble_sort_op = BigO('Bubble Sort')
    plotter = Plotter()
    plotter.add_object(bubble_sort_op)

    # Create an array with different length N times
    for i in range(1000):

        # Create random array with length of i+1
        unsorted_array = np.random.randint(0, i + 1, size=i + 1)

        # Sort an array by calling bubble_sort function
        bubble_sort_op.time_function(bubble_sort, array=unsorted_array)

    # Plot the performance
    plotter.to_plot()

def bubble_sort(array):
    """
    Implementation of the bubble sort which runs in O(N^2) in runtime and O(1) in space
    Args:
        array: an unsorted array where each element has integer data type
    Returns:
        list<int>: sorted version of the input array
    """
    # Loop through the array one by one
    for i in range(len(array)):

        # Loop through the array where elements aren't in the right position
        for j in range(len(array) - i - 1):

            # Swap the adjacent elements if they aren't in order
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

if __name__ == '__main__':
    main()
