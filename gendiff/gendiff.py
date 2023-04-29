import json


def load_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def compare_json_files(file1, file2):
    keys = file1.keys() | file2.keys()
    return [(key, file1.get(key), file2.get(key)) for key in sorted(keys)]


def format_diff(key, val1, val2):
    if val1 == val2:
        return f'    {key}: {val1}\n'
    elif val1 is None:
        return f'  + {key}: {val2}\n'
    elif val2 is None:
        return f'  - {key}: {val1}\n'
    else:
        return f'  - {key}: {val1}\n  + {key}: {val2}\n'


def generate_diff(file_path1, file_path2):
    file1 = load_json_file(file_path1)
    file2 = load_json_file(file_path2)
    diff = [format_diff(*vals) for vals in compare_json_files(file1, file2)]
    return '{\n' + ''.join(diff).lower() + '}'
