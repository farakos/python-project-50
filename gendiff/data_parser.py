import json
import yaml


def load_file(file_path):
    extention = file_path.split('.')[-1]
    with open(file_path, 'r') as f:
        if extention == 'json':
            return json.load(f)
        elif extention in ['yml', 'yaml']:
            return yaml.load(f, Loader=yaml.CLoader)
        else:
            return {}


def parse_data(file_path1, file_path2):
    print(load_file(file_path1))
    print(load_file(file_path2))
    return load_file(file_path1), load_file(file_path2)
