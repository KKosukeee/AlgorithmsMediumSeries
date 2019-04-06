"""
    Part 1 of blog post contents are within this file
"""
from classes import BigO, CallableConfig

def main():
    """
    main function

    Returns:

    """

    # Implement constant time lookup
    bigo = BigO()
    config = CallableConfig(
        [0, 1000],
        data={'type': list, 'range': [0, 100]},
        index={'type': int, 'range': [0, 100]}
    )

    bigo.approximate(lookup, config)
    bigo.to_plot()

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

if __name__ == '__main__':
    main()
