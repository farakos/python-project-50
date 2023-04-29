import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1, 'r'))
    file2 = json.load(open(file_path2, 'r'))
    keys = file1.keys() | file2.keys()
    diff = ''

    for key in keys:
        if key in file1:

            if key in file2:

                if file1[key] == file2[key]:
                    diff += f'    {key}: {file1[key]}\n'
                else:
                    diff += f'  - {key}: {file1[key]}\n'
                    diff += f'  + {key}: {file2[key]}\n'

            else:
                diff += f'  - {key}: {file1[key]}\n'

        else:
            diff += f'  + {key}: {file2[key]}\n'

    return '{\n' + diff + '}'

