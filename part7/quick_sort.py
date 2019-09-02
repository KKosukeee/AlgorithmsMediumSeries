"""
This file contains a content for the part 7 of the data structures and algorithms series
"""
import numpy as np
from classes import BigO
from classes import Plotter

def main():
    """
    Main function of this file. It runs a quick sort several times

    Returns:
        None:

    """
    # Initialize quick sort operation to see the runtime
    quick_sort_op = BigO('Quick Sort')
    plotter = Plotter()
    plotter.add_object(quick_sort_op)

    # Create an array with different length N times
    for i in range(1000):
        # Create an arbitrary array
        unsorted_array = np.random.randint(0, i+1, size=i+1)
        # Sort an array by calling quick_sort function
        quick_sort_op.time_function(quick_sort, array=unsorted_array, low=0, high=i)

    # Plot the runtime
    plotter.to_plot()

def quick_sort(array, low, high):
    """
    This function sorts an array via quick sort. This function calls itself (recursion) with the
    pivot pointer returned by the partition function

    Args:
        array(list[int]): list of integers to sort
        low(int): int value representing the left-most index where the elements in the range are unsorted
        high(int): int value representing the right-most index as opposed to the left-most (low)

    Returns:
        None:

    """
    if not low < high:
        return
    # After this function call, array[pivot] will be in the right position
    pivot = partition(array, low, high)
    # Recursively call for the left-half of the array
    quick_sort(array, low, pivot-1)
    # Recursively call for the right-half of the array
    quick_sort(array, pivot+1, high)

def partition(array, low, high):
    """
    This function partitions an array in memory, such that

    Args:
        array(lit[int]): list of integers to partition with
        low(int): a pointer which points the left-most element that isn't in-place yet
        high(int): a pointer which points the right-most element that isn't in-place yet

    Returns:
        int: int value representing the pivot number where array[pivot] is in the right position

    """
    i = low
    pivot = array[high]
    # Loop for each number in the range [low, high)
    for j in range(low, high):
        # If current number is smaller than the pivot, then swap them
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    # After the loop, I know where the pivot should go, just swap them
    array[i], array[high] = array[high], array[i]
    return i

if __name__ == '__main__':
    main()
