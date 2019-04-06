"""
    BigO object to approximate the run time complexity
"""
import time
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
style.use('ggplot')

class BigO:
    """
        BigO object implementation
    """

    def __init__(self):
        """
            Initialization method
        """
        self.complexity = None

    def approximate(self, function, config):
        """
        Approximate function f with input of x. It will plot, but now showing it,
        unless self.to_plot method is called

        Args:
            function: a callable object to approximate time complexity
            config: CallableConfig object.

        Returns:

        """
        # Create a list to store elapsed time
        elapsed_times = []

        # Loop config.how_many times
        for params in config.get_params():

            # Run the function with config.get_params
            start = time.time()
            function(**params)
            end = time.time()

            # Store elapsed time into the list
            elapsed_times.append(end - start)

        # Plot run time complexity with x-axis being # of elements in the data
        elapsed_times = np.array(elapsed_times)
        plt.plot(np.arange(elapsed_times.size), elapsed_times)

    def to_plot(self):
        """
        It will plot the run time complexity given by self.approximate method.

        Returns:

        """
        plt.show()

    def to_png(self, path_obj):
        """
        This method will save a png image plotting run time complexity.

        Args:
            path_obj: path object determine where to save the image

        Raises:

        """
        plt.savefig(str(path_obj))
