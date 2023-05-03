import json as j
from gendiff import BOOLS


def replace_bool(value):
    for key, bool_value in BOOLS.items():
        if value == bool_value:
            value = key
    return value


def format_dict(list_diff):
    dictionary = {}
    for node in list_diff:
        _, status, key, value = node
        json_key = f'[{status}] {key}'
        if not isinstance(value, list):
            json_value = replace_bool(value)
        else:
            json_value = format_dict(value)
        dictionary[json_key] = json_value
    return dictionary


def json(nested_diff):
    dict_diff = format_dict(nested_diff)
    return j.dumps(dict_diff, indent=2)
