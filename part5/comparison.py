"""
This file compares the runtime for recursive Fibonacci and DP Fibonacci.
Read the fifth post in the Data Structures and Algorithms series to see the full content
"""

from classes import BigO
from classes import Plotter
from part5.recursions import fibonacci as recursion
from part5.dps import fibonacci as dp

def main():
    """
    Main function of this file
    Returns:

    """
    # Initialize BigO object for calculating the run times
    recursive_fibonacci = BigO('Recursive Fibonacci')
    dp_fibonacci = BigO('DP Fibonacci')
    plotter = Plotter()
    plotter.add_objects(recursive_fibonacci, dp_fibonacci)

    # Loop through N times to create length of array ranging [1, N]
    for i in range(30):
        recursive_fibonacci.time_function(recursion, n=i+1)
        dp_fibonacci.time_function(dp, n=i+1, memo={})

    # Plot both run times to compare
    plotter.to_plot()

if __name__ == '__main__':
    main()
