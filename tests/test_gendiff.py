from pathlib import Path

import pytest

from gendiff.generate_diff import generate_diff

TEST_DATA_DIR = Path(__file__).parent / "test_data"

TEST_PARAMS = [
    ("file1.json", "file2.json", "stylish", "stylish_plain.txt"),
    ("file1.yaml", "file2.yaml", "stylish", "stylish_plain.txt"),
    ("file1_tree.json", "file2_tree.json", "stylish", "stylish_tree.txt"),
    ("file1_tree.yaml", "file2_tree.yaml", "stylish", "stylish_tree.txt"),
    ("file1_tree.json", "file2_tree.json", "plain", "plain_tree.txt"),
    ("file1_tree.yaml", "file2_tree.yaml", "plain", "plain_tree.txt"),
    ("file1_tree.json", "file2_tree.json", "json", "json_tree.txt"),
    ("file1_tree.yaml", "file2_tree.yaml", "json", "json_tree.txt"),
]


def get_test_data_path(filename):
    return str(TEST_DATA_DIR / filename)


def read_file(filename):
    path = get_test_data_path(filename)
    with open(path, "r") as f:
        return f.read()


@pytest.mark.parametrize("path1, path2, format, expected", TEST_PARAMS)
def test_gendiff_json(path1, path2, format, expected):
    expected_result = read_file(expected)
    test_result = generate_diff(
        get_test_data_path(path1), get_test_data_path(path2), format
    )

    assert expected_result == test_result
