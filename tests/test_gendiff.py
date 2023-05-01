from gendiff.gendiff import generate_diff
import json
import yaml


def test_generate_diff():
    with open('tests/fixtures/result.txt', 'r') as f:
        expected = f.read()[:-1]
    with open('tests/fixtures/file1.json', 'r') as j1:
        json_file1 = json.load(j1)
    with open('tests/fixtures/file2.json', 'r') as j2:
        json_file2 = json.load(j2)
    with open('tests/fixtures/file1.yml', 'r') as y1:
        yaml_file1 = yaml.load(y1, Loader=yaml.CLoader)
    with open('tests/fixtures/file2.yml', 'r') as y2:
        yaml_file2 = yaml.load(y2, Loader=yaml.CLoader)

    json_result = generate_diff(json_file1, json_file2)
    yaml_result = generate_diff(yaml_file1, yaml_file2)

    assert json_result == expected
    assert yaml_result == expected


def test_generate_diff_nested():
    with open('tests/fixtures/result_nested.txt', 'r') as f:
        expected = f.read()[:-1]
    with open('tests/fixtures/nested_file1.json', 'r') as j1:
        json_file1 = json.load(j1)
    with open('tests/fixtures/nested_file2.json', 'r') as j2:
        json_file2 = json.load(j2)

    json_result = generate_diff(json_file1, json_file2)

    assert json_result == expected
