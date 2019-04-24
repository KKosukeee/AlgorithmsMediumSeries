"""
    BigO object to approximate the run time complexity
"""
import time
import matplotlib.pyplot as plt
import numpy as np

class BigO:
    """
        BigO object implementation
    """

    def __init__(self, funcname):
        """
        Initialization method
        Args:
            funcname: function name to be displayed
        """
        self.complexity = None
        self.kernel_size = 9
        self.elapsed_times = []
        self.funcname = funcname

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
        kernel = np.ones(self.kernel_size) / float(self.kernel_size)
        elapsed_times = np.array(self.elapsed_times)
        smoothed = np.convolve(elapsed_times, kernel, mode='same')
        plt.plot(np.arange(smoothed.size), smoothed, label=self.funcname)
        plt.legend(facecolor='white')

    def to_png(self, path_obj):
        """
        This method will save a png image plotting run time complexity.

        Args:
            path_obj: path object determine where to save the image

        Raises:

        """
        plt.plot(np.arange(len(self.elapsed_times)), np.array(self.elapsed_times))
        plt.savefig(str(path_obj))
