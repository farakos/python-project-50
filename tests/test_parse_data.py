from gendiff.data_parser import parse_data
import json
import yaml


def test_generate_diff():
    with open('tests/fixtures/file1.json', 'r') as j1:
        json_file1 = json.load(j1)
    with open('tests/fixtures/file2.json', 'r') as j2:
        json_file2 = json.load(j2)
    with open('tests/fixtures/file1.yml', 'r') as y1:
        yaml_file1 = yaml.load(y1, Loader=yaml.CLoader)
    with open('tests/fixtures/file2.yml', 'r') as y2:
        yaml_file2 = yaml.load(y2, Loader=yaml.CLoader)

    json_result = parse_data(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            )
    yaml_result = parse_data(
            'tests/fixtures/file1.yml',
            'tests/fixtures/file2.yml',
            )

    assert json_result == (json_file1, json_file2)
    assert yaml_result == (yaml_file1, yaml_file2)
