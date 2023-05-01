from gendiff.constants import MARGIN, MARGIN_MULTIPLIER


def compare_files(file1, file2):
    keys = file1.keys() | file2.keys()
    result = []
    for key in sorted(keys):
        value1 = value2 = None
        if key in file1.keys():
            value1 = 'null' if file1[key] is None else file1[key]
        if key in file2.keys():
            value2 = 'null' if file2[key] is None else file2[key]
        result.append((key, value1, value2))
    return result


def generate_nested_diff(node1, node2, depth=1):
    indent = MARGIN * (MARGIN_MULTIPLIER * depth - 1)
    nested_diff = []

    for key, value1, value2 in compare_files(node1, node2):
        if value1 == value2:
            nested_diff.append([indent + MARGIN, key, value1])
        elif value1 is None:
            nested_diff.append([indent + '+ ', key, value2])
        elif value2 is None:
            nested_diff.append([indent + '- ', key, value1])
        elif not isinstance(value1, dict) or not isinstance(value2, dict):
            nested_diff.append([indent + '- ', key, value1])
            nested_diff.append([indent + '+ ', key, value2])
        else:
            nested_diff.append(
                [
                    indent + MARGIN,
                    key,
                    generate_nested_diff(value1, value2, depth + 1)
                ]
            )
    return nested_diff


def format_value(value, indent):
    result = ''
    if not isinstance(value, dict):
        result += ' ' if value != '' else ''
        result += str(value).lower() if isinstance(value, bool) else str(value)
        result += '\n'
    else:
        result += ' {\n'
        for key, val in value.items():
            result += f'{indent}{MARGIN * MARGIN_MULTIPLIER}{key}:'
            result += format_value(val, indent + MARGIN * MARGIN_MULTIPLIER)
        result += indent + '}\n'
    return result


def format_diff(diff):
    result = ''
    for indent, key, value in diff:
        result += indent + f'{key}:'
        if not isinstance(value, list):
            result += format_value(value, indent[:-2] + MARGIN)
        else:
            result += ' {\n'
            result += format_diff(value)
            result += indent + '}\n'
    return result


def generate_diff(file1, file2):
    nested_diff = generate_nested_diff(file1, file2)
    result = '{\n' + format_diff(nested_diff) + '}'
    return result
