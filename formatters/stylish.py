from gendiff import MARGIN, MARGIN_MULTIPLIER, SIGN


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


def stylish(nested_diff):
    result = '{\n' + format_diff(nested_diff) + '}'
    return result
