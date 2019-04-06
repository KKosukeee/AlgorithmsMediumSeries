"""
    A config for callable in BigO.approximate
"""
import numpy as np

class CallableConfig:
    """
        Implementation for callable config object
    """

    def __init__(self, data_range, **kwargs):
        """
        Initialization method

        Args:
            call_times: times you wanna call the callable object
            data_range: range of data represented in list. list[0] is min, and list[-1] is max
            **kwargs: kwarge being same key as callable's parameter, and value
        """
        self.data_range = data_range
        self.kwargs = kwargs
        self.call_times = abs(data_range[1] - data_range[0])

        # Create generator with calling self.call_times


    def get_params(self):
        """
        Call this method to get parameters.

        Returns:
            generator: each value is input to the function
        """

        pass
