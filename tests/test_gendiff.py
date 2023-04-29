from gendiff.gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/result.txt', 'r') as f:
        expected = f.read()[:-1]

    result = generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json'
            )
    assert result == expected
