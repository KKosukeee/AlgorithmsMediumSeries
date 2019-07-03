"""
Implementation of the merge sort in the part 6 of the Data Structures and Algorithms series
"""
import numpy as np
from classes import BigO
from classes import Plotter

def main():
    """
    Main function for this file
    Returns:

    """
    merge_sort_op = BigO('Bubble Sort')
    plotter = Plotter()
    plotter.add_object(merge_sort_op)

    # Create an array with different length N times
    for i in range(1000):
        # Create random array with length of i+1
        unsorted_array = np.random.randint(0, i + 1, size=i + 1)

        # Sort an array by calling bubble_sort function
        merge_sort_op.time_function(merge_sort, array=unsorted_array)

    # Plot the performance
    plotter.to_plot()

def merge_sort(array):
    """
    Merge sort implementation. The input is an unsorted array, which will be sorted in return
    Args:
        array: list of integers where elements are not sorted
    Returns:
        list<int>: list of integers where elements are sorted
    """
    if len(array) <= 1:
        return array

    # A pointer for dividing an array in half
    middle = len(array) // 2
    sorted_array = []

    # Divide an array in a half, then sort divided sub-arrays recursively
    left_half = merge_sort(array[:middle])
    right_half = merge_sort(array[middle:])

    # Initialize pointers for left and right half array
    i, j = 0, 0

    # Loop while both pointers are in the range
    while i < len(left_half) and j < len(right_half):
        # Put an element from either left or right, according to the comparison
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1

    # If elements are left, then put them into the array
    while i < len(left_half):
        sorted_array.append(left_half[i])
        i += 1

    # Do above operation for the right half as well
    while j < len(right_half):
        sorted_array.append(right_half[j])
        j += 1

    return sorted_array

if __name__ == '__main__':
    main()
