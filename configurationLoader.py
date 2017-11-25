import json


def load_configuration_file(file_name):
    with open(file_name) as configuration_file:
        return json.load(configuration_file)