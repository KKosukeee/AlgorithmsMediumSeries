"""
    All implementation code within what are algorithms section is in this file
"""
import numpy as np
from classes import BigO

def main():
    """
    main function

    Returns:

    """
    naive_bigo = BigO()
    optimal_bigo = BigO()

    for i in range(1000):
        data = np.random.randint(0, 10, size=i+1)
        target = np.random.randint(0, i + 1)

        # naive solution
        naive_bigo.time_function(naive_approach, data=data, target=target)

        # optimal solution
        optimal_bigo.time_function(optimal_approach, data=data, target=target)

    naive_bigo.to_plot()
    optimal_bigo.to_plot()

def naive_approach(data, target):
    """
    Implement naive approach which in result being O(n^2)

    Args:
        data: a list to find a target from
        target: value you want to find by adding data[x] and data[y]

    Returns:
        list<int>: list of integer value from data. List of -1 will be return in case there
            isn't values add up to target
    """

    # Loop through data
    for i, first_item in data:

        # Loop through data from index i + 1
        for _, second_item in enumerate(data[i + 1:]):

            # If data[i] + data[j] == target, then return
            if first_item + second_item == target:
                return first_item, second_item

    return -1, -1

def optimal_approach(data, target):
    """
    Implementation of optimal solution which run in O(n)

    Args:
        data: a list of integer.
        target: target value which you try to find data[x] + data[y] == target

    Returns:
        list<int>: list of int such that sum(list) equals to target. If there aren't such values,
            return list of -1
    """

    # Initialize comp dictionary
    comp = set()

    # Loop through data
    for value in data:

        # If data[i] isn't in comp, then add
        if value not in comp:
            comp.add(target - value)

        # Otherwise, you found the solution
        else:
            return value, target - value

    return -1, -1

if __name__ == '__main__':
    main()
