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
        self.elapsed_times = []

    def approximate(self):
        """
        Finds the most similar function given x == range(1, len(self.elapsed_times)
        and y = self.elapsed_times

        Returns:

        """


    def time_function(self, function, **kwargs):
        """
        Time how long it takes to run callable function given kwargs

        Args:
            function: a callable function where you call callable(**kwargs)
            **kwargs: parameters for callable function.

        Returns:

        """
        start = time.time()
        function(**kwargs)
        end = time.time()
        self.elapsed_times.append(end - start)

    def to_plot(self):
        """
        It will plot the run time complexity given by self.approximate method.

        Returns:

        """
        plt.plot(np.arange(len(self.elapsed_times)), np.array(self.elapsed_times))
        plt.show()

    def to_png(self, path_obj):
        """
        This method will save a png image plotting run time complexity.

        Args:
            path_obj: path object determine where to save the image

        Raises:

        """
        plt.plot(np.arange(len(self.elapsed_times)), np.array(self.elapsed_times))
        plt.savefig(str(path_obj))
