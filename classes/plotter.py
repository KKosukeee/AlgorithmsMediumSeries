"""
    Plotter object for better visualization
"""
import matplotlib.pyplot as plt
from matplotlib import style
from classes import BigO
style.use('ggplot')

class Plotter:
    """
        Plotter class for visualizing multiple run times
    """
    def __init__(self, title='Runtime comparison'):
        """
        Initialization method

        Args:
            title: title for the plot
        """
        self.title = title
        self.bigos = []

    def add_object(self, bigo):
        """
        Registration function for visualization. All the

        Args:
            bigo: BigO object to plot later.

        Returns:

        Raises:
            TypeError: if bigo is not an instance of BigO
        """
        if not isinstance(bigo, BigO):
            raise TypeError('input to add_object method need an instance of BigO object')

        self.bigos.append(bigo)

    def add_objects(self, *args):
        """
        Registration function for multiple big objects.

        Args:
            *args: multiple BigO objects to plot later for comparison

        Returns:

        Raises:
            TypeError: if either one of args is not BigO object
        """

        for bigo in args:
            self.add_object(bigo)

    def to_plot(self):
        """
        It will plot the run time complexity given by self.approximate method.

        Returns:

        """

        for bigo in self.bigos:
            bigo.to_plot()

        plt.title(self.title)
        plt.xlabel('# of elements')
        plt.ylabel('Execution time in seconds')
        plt.grid(False)
        plt.show()

    def to_png(self, path):
        """
        This method will save a png image plotting run time complexity.

        Args:
            path: path object determine where to save the image

        Raises:

        """
