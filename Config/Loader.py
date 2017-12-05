import json
import os


def load_configuration_file(file_name):
    with open(os.getcwd() + "/" + file_name) as configuration_file:
        return json.load(configuration_file)


def save_json_file(file_name, data):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def filter_list_manually_boolean(items, question_string, attribute=False):
    selected_items = []
    for item in items:
        __manual_boolean_selector(item, selected_items, question_string, attribute)
    return selected_items


def __manual_boolean_selector(item, selected_items, question_string, attribute):
    if attribute:
        display_item = getattr(item, attribute)
    else:
        display_item = item
    print(question_string + " (y/N) -- " + display_item)
    user_input = input()
    if user_input == "n" or user_input == "N" or user_input == "":
        'do nothing'
    elif user_input == "y" or user_input == "Y":
        selected_items.append(item)
    else:
        print("Invalid input, try again!")
        __manual_boolean_selector(item, selected_items)


def retrieve_index_manually_from_list(items, question_string, attribute=False):
    print(question_string)
    print("index        name")
    for index, item in enumerate(items):
        if attribute:
            display_item = item[attribute]
        else:
            display_item = item
        print(str(index) + "        " + str(display_item))
    return __manual_list_index_selector(items)


def __manual_list_index_selector(items):
    try:
        user_input = int(input("Select a number between 0 and " + str(len(items) - 1) + ": "))
        if 0 <= user_input < len(items):
            return items[user_input]
        else:
            print("Invalid input, try again!")
            __manual_list_index_selector(items)
    except Exception:
        print("Invalid input, try again!")
        __manual_list_index_selector(items)
