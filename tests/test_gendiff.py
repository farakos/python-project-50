from gendiff.gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/result.txt', 'r') as f:
        expected = f.read()[:-1]
    json_path1 = 'tests/fixtures/file1.json'
    json_path2 = 'tests/fixtures/file2.json'
    yaml_path1 = 'tests/fixtures/file1.yml'
    yaml_path2 = 'tests/fixtures/file2.yml'

    assert generate_diff(json_path1, json_path2) == expected
    assert generate_diff(yaml_path1, yaml_path2) == expected


def test_generate_diff_nested():
    with open('tests/fixtures/result_nested.txt', 'r') as f:
        expected = f.read()[:-1]
    with open('tests/fixtures/result_nested_plain.txt', 'r') as f:
        expected_plain = f.read()[:-1]
    with open('tests/fixtures/result_nested_json.txt', 'r') as f:
        expected_json = f.read()[:-1]

    json_path1 = 'tests/fixtures/nested_file1.json'
    json_path2 = 'tests/fixtures/nested_file2.json'
    yaml_path1 = 'tests/fixtures/nested_file1.yaml'
    yaml_path2 = 'tests/fixtures/nested_file2.yaml'

    assert generate_diff(json_path1, json_path2) == expected
    assert generate_diff(yaml_path1, yaml_path2) == expected

    assert generate_diff(json_path1, json_path2, 'plain') == expected_plain
    assert generate_diff(yaml_path1, yaml_path2, 'plain') == expected_plain

    assert generate_diff(json_path1, json_path2, 'json') == expected_json
    assert generate_diff(yaml_path1, yaml_path2, 'json') == expected_json
