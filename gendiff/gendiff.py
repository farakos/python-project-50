from gendiff.constants import MARGIN, MARGIN_MULTIPLIER, SIGN


def define_value(key, file):
    if key in file.keys():
        value = file[key]
        if value is None:
            return 'null'
        return str(value).lower() if isinstance(value, bool) else value
    return None


def compare_files(file1, file2):
    keys = file1.keys() | file2.keys()
    return [
            (key, define_value(key, file1), define_value(key, file2))
            for key in sorted(keys)
            ]


def generate_nested_diff(node1, node2, depth=1):
    nested_diff = []

    for key, value1, value2 in compare_files(node1, node2):
        if value1 == value2:
            nested_diff.append([depth, 'unchanged', key, value1])
        elif value1 is None:
            nested_diff.append([depth, 'added', key, value2])
        elif value2 is None:
            nested_diff.append([depth, 'removed', key, value1])
        elif not isinstance(value1, dict) or not isinstance(value2, dict):
            nested_diff.append([depth, 'removed', key, value1])
            nested_diff.append([depth, 'added', key, value2])
        else:
            nested_diff.append(
                [
                    depth, 'changed',
                    key,
                    generate_nested_diff(value1, value2, depth + 1)
                ]
            )
    return nested_diff


def get_value_space(value):
    return '' if value == '' else ' '


def format_value(value, indent):
    result = ''
    if not isinstance(value, dict):
        result += f'{get_value_space(value)}{value}\n'
    else:
        result += ' {\n'
        for key, val in value.items():
            result += f'{indent}{MARGIN * MARGIN_MULTIPLIER}{key}:'
            result += format_value(val, indent + MARGIN * MARGIN_MULTIPLIER)
        result += indent + '}\n'
    return result


def format_diff(diff):
    result = ''
    for depth, status, key, value in diff:
        indent = MARGIN * (MARGIN_MULTIPLIER * depth - 1)
        result += indent + SIGN[status] + f'{key}:'
        if not isinstance(value, list):
            result += format_value(value, indent + MARGIN)
        else:
            result += ' {\n'
            result += format_diff(value)
            result += indent + MARGIN + '}\n'
    return result


def generate_diff(file1, file2):
    nested_diff = generate_nested_diff(file1, file2)
    result = '{\n' + format_diff(nested_diff) + '}'
    return result
