"""
    All implementation code within what are algorithms section is in this file
"""
import numpy as np
from classes import BigO, Plotter

def main():
    """
    main function

    Returns:

    """
    plotter = Plotter()
    naive_bigo = BigO('Naive algorithm')
    optimal_bigo = BigO('Optimal algorithm')
    plotter.add_objects(naive_bigo, optimal_bigo)

    for i in range(1000):
        nums = np.random.randint(0, 10, size=i+1)
        target = np.random.randint(0, i + 1)

        # naive solution
        naive_bigo.time_function(naive_approach, nums=nums, target=target)

        # optimal solution
        optimal_bigo.time_function(optimal_approach, nums=nums, target=target)

    plotter.to_plot()

# Brute force approach: O(n^2)
def naive_approach(nums, target):
    """
    solves two sum problem

    Args:
        nums: list of numbers to search from
        target: target number to add up to

    Returns:
        list: containing indices for numbers which add up to target
    """
    # Loop through nums,
    for i in range(len(nums)):

        # Loop through nums AGAIN
        for j in range(i+1, len(nums)):

            # If target == nums[i] + nums[j], then return indices
            if target == nums[i] + nums[j]:
                return [i, j]

    return []

# Optimal solution: O(n)
def optimal_approach(nums, target):
    """
    solves two sum problem
    Args:
        nums: list of numbers to search from
        target: target number to add up to
    Returns:
        list: containing indices for numbers which add up to target
    """

    # Create complement_dictionary being complement as key, and index as value
    complement_dictionary = {}  # O(1)

    # Loop through nums
    for i in range(len(nums)):  # O(n)

        # If target - num[i] exists in the complement_dictionary, then return indices
        if target - nums[i] in complement_dictionary:  # O(1)
            return [complement_dictionary[target - nums[i]], i]  # O(1)

        # Store index value with key of target - nums[i]
        complement_dictionary[nums[i]] = i  # O(1)

    return []

if __name__ == '__main__':
    main()
