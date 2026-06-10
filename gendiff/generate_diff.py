import json


def format_value(value):
    if isinstance(value, bool):
        if value:
            return "true"
        else:
            return "false"
    else:
        return value


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    keys1 = data1.keys()
    keys2 = data2.keys()

    all_keys = keys1 | keys2
    sorted_keys = sorted(all_keys)

    data_diff = []

    for key in sorted_keys:
        if key in keys1 & keys2:
            if data1[key] == data2[key]:
                data_diff.append(f"    {key}: {format_value(data1[key])}")
            else:
                data_diff.append(f"  - {key}: {format_value(data1[key])}")
                data_diff.append(f"  + {key}: {format_value(data2[key])}")
        elif key in keys1:
            data_diff.append(f"  - {key}: {format_value(data1[key])}")
        else:
            data_diff.append(f"  + {key}: {format_value(data2[key])}")

    result = f"{{\n{'\n'.join(data_diff)}\n}}"

    return result
