from gendiff.constants import BOOLS


def form_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str) and value not in BOOLS.values():
        return f"'{value}'"
    else:
        return f'{value}'


def is_updated(node):
    return node[1] != 'unchanged'


def update_diff_list(nested_diff, diff_list, path=''):
    line = ''
    nested_diff = filter(is_updated, nested_diff)
    for _, status, key, value in nested_diff:
        if isinstance(value, list):
            update_diff_list(value, diff_list, f'{path}{key}.')

        elif status == 'update.removed':
            line = f"Property '{path}{key}' was updated. "
            line += f"From {form_value(value)} "

        elif status == 'update.added':
            line += f'to {form_value(value)}'
            diff_list.append(line)

        else:
            line = f"Property '{path}{key}' was {status}"
            if status == 'added':
                line += f" with value: {form_value(value)}"
            diff_list.append(line)


def plain(nested_diff):
    diff_list = []
    update_diff_list(nested_diff, diff_list)
    return '\n'.join(diff_list)
