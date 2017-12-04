import json
import os


def load_configuration_file(file_name):
    with open(os.getcwd() + "/" + file_name) as configuration_file:
        return json.load(configuration_file)


def save_json_file(file_name, data):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def filter_list_manually(list, object_name, attribute):
    kept = []
    for item in list:
        __manual_selector(item, kept, object_name, attribute)
    return kept


def __manual_selector(item, selected_objects, question, attribute):
    print(question + " (y/N) -- " + item[attribute])
    user_input = input()
    if user_input == "n" or user_input == "N" or user_input == "":
        'do nothing'
    elif user_input == "y" or user_input == "Y":
        selected_objects.append(item)
    else:
        print("Invalid input, try again!")
        __manual_selector(item, selected_objects)
