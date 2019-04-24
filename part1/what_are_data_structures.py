"""
    Part 1 of blog post contents are within this file
"""
import numpy as np
import matplotlib.pyplot as plt
from classes import BigO, Plotter

def main():
    """
    main function

    Returns:

    """

    # Implement constant time lookup
    array_lookup = BigO('Array lookup')

    plotter = Plotter()
    plotter.add_object(array_lookup)

    for i in range(1000):
        data = np.random.randint(0, 1000, size=i+1)
        index = np.random.randint(0, i) if i else 0
        array_lookup.time_function(lookup, data=data.tolist(), index=index)

    plt.ylim((1e-7 - 1e-5, 1e-7 + 1e-5))
    plotter.to_plot()

def lookup(data, index):
    """
    Look up data[index], and return it.

    Args:
        data: list<int> object.
        index: int to get an element from data list

    Returns:
        int: a value from data with index value specified

    Raises:
        IndexError: if index is not in the range of 0 <= index < len(data)
    """
    return data[index]

def insert(data, index, element):
    """
    Insertion operation for an array

    Args:
        data: list<int> object.
        index: an index value to insert element
        element: an element to insert at index

    Returns:
        list: list after the insertion

    Raises:

    """
    return data.insert(index, element)

if __name__ == '__main__':
    main()
