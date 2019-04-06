"""
    All implementation code within what are algorithms section is in this file
"""

def main():
    """
    main function

    Returns:

    """
    pass

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
    for i, x in enumerate(data):

        # Loop through data from index i + 1
        for _, v in enumerate(data[i + 1:]):

            # If data[i] + data[j] == target, then return
            if x + v == target:
                return x, v

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
    comp = {}

    # Loop through data
    for _, x in enumerate(data):

        # If data[i] isn't in comp, then add
        if x not in comp:
            comp[target - comp] = x

        # Otherwise, you found the solution
        else:
            return x, comp[x]

    return -1, -1

if __name__ == '__main__':
    main()
