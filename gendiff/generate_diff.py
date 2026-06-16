import json


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f:
        data1 = json.load(f)
    with open(file_path2) as f:
        data2 = json.load(f)

    keys1 = data1.keys()
    keys2 = data2.keys()

    all_keys = keys1 | keys2
    sorted_keys = sorted(all_keys)
    common_keys = keys1 & keys2
    added_keys = keys2 - keys1
    deleted_keys = keys1 - keys2

    data_diff = []

    for key in sorted_keys:
        if key in common_keys:
            if data1[key] == data2[key]:
                data_diff.append(f"    {key}: {format_value(data1[key])}")
            else:
                data_diff.append(f"  - {key}: {format_value(data1[key])}")
                data_diff.append(f"  + {key}: {format_value(data2[key])}")
        elif key in added_keys:
            data_diff.append(f"  + {key}: {format_value(data2[key])}")
        elif key in deleted_keys:
            data_diff.append(f"  - {key}: {format_value(data1[key])}")

    result = f"{{\n{'\n'.join(data_diff)}\n}}"

    return result
