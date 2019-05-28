"""
This file has an implementation for recursions section in the part 5 of
the Data structures and Algorithms series
"""

def main():
    """
    Main function of the file
    Returns:

    """

def fibonacci(n):
    """
    Calculates the n-th fibonacci sequence
    Args:
        n: positive int value to calculate n-th fibonacci sequence
    Returns:
        int: representing the value of n-th fibonacci sequence
    """
    if n < 2:
        return 0 if n < 0 else 1

    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    main()
