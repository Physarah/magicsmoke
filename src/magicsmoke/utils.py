# It's a good idea to have a general utils module that you can import for functional things.
# In this example, I've included an example function that will import your config file as
# a dictionary
import yaml
import os


def load_config(config_path):

"""
A general yaml config parser

    Inputs:
        config_path(str): the path to the config file
    Returns:
        config_dictionary(dict): a dictionary of the config file
"""
   with open(config_path) as open_file:
        config_dictionary = yaml.safe_load(open_file)
    return(config_dictionary)
