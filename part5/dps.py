"""
This file solves nth Fibonacci sequence using a technique called Dynamic programming
What the function does is identical to the recursive one, but it runs much faster.
"""

def main():
    """
    Main function of this file
    Returns:

    """

def fibonacci(n, memo):
    """
    Calculates the n-th fibonacci sequence using Dynamic Programming
    Args:
        n: positive int value to calculate n-th fibonacci sequence
        memo: dict storing nth Fibonacci as key and value pair.
    Returns:
        int: representing the value of n-th fibonacci sequence
    """
    if n < 2:
        return 0 if n < 0 else 1

    if n in memo:
        return memo[n]

    memo[n - 1] = fibonacci(n - 1, memo)
    memo[n - 2] = fibonacci(n - 2, memo)
    memo[n] = memo[n - 1] + memo[n - 2]
    return memo[n]

if __name__ == '__main__':
    main()
