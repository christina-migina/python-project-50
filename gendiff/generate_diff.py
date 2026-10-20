from gendiff.parser import parse
from gendiff.builder import build_diff
from gendiff.formatters.selector import formatter_selector


def generate_diff(file_path1, file_path2, formatter_name='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)

    diff = build_diff(data1, data2)
    formatted_diff = formatter_selector(diff, formatter_name)

    return formatted_diff
