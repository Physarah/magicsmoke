# Can be imported as "from magicsmoke.example_module_1 import function_1"
# Put your classes/functions in here
import os
import numpy as np
from magicsmoke.utils import load_config


class ExampleClass():

    """
    This is an example class template
        Inputs:
            input1 (int): example input1
            input2 (str): example input2
            input3 (int): example input3
        Attributes:
            attribute1 (int): example attribute
            package_location (str): location of package install
            package_asset_path (str): path to text file example
            config (dict): dictronary from imported yaml file
    """

   def __init__(self, input1, input2, input3):
        self.input1 = input1  # self is needed here so it came be passed to other methods
        self.input2 = input2
        self.input3 = input3
        # Do something with the input params if you like in the __init__
        if self.input1 == self.input3:
            self.attribute1 = self.input1 + self.input3
        # Example of grabbing data files from assets
        self.package_location = os.path.dirname(os.path.realpath(__file__))
        self.package_asset_path = os.path.join(self.package_location, 'assets', 'example_asset.txt')
        # Example of importing config files
        self.config = load_config(os.join(self.package_location, 'config', 'example_config.yaml')

    def example_method(self):
        """
        Example method inside a class
            Returns:
                output (int): example output

        """
        for i in np.arange(0, 100):
            print(self.input3)
        output = self.input1 # output cannot be accessed by other methods etc as it has no self
        return(output)

    def example_method_2(self, input4, input5):
        """
        Another class example with other inputs
            Inputs:
                input4 (int): example input4
                input5 (int): example input5
            Returns:
                output2 (int): example output2
        """
        output2 = input4 + self.attribute1 # you can use self. things as normal variables throughout the entire class
        return(output2)
