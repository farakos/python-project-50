import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1, 'r'))
    file2 = json.load(open(file_path2, 'r'))
    keys = set(file1) | set(file2)
    diff = ''

    for key in keys:
        if key in file1:
            value1 = file1[key]
            if key in file2:
                value2 = file2[key]
                if value1 == value2:
                    diff += f'    {key}: {value1}\n'
                else:
                    diff += f'  - {key}: {value1}\n'
                    diff += f'  + {key}: {value2}\n'
            else:
                diff += f'  - {key}: {value1}\n'
        else:
            value2 = file2[key]
            diff += f'  + {key}: {value2}\n'

    return '{\n' + diff + '}'
