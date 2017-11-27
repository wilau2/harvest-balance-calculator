import json
import os


def load_configuration_file(file_name):
    with open(os.getcwd() + "/" + file_name) as configuration_file:
        return json.load(configuration_file)
