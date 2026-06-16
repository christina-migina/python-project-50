from pathlib import Path
from gendiff.generate_diff import generate_diff

test_data = Path(__file__).parent / "test_data"


def test_gendiff():
    with open(test_data / "result.txt") as f:
        content = f.read()

    test_result = generate_diff(test_data / "file1.json", test_data / "file2.json")

    assert content == test_result
