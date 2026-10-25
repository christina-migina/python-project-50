def build_diff(data1, data2):
    keys1 = data1.keys()
    keys2 = data2.keys()

    all_keys = keys1 | keys2
    sorted_keys = sorted(all_keys)
    common_keys = keys1 & keys2
    added_keys = keys2 - keys1
    deleted_keys = keys1 - keys2

    diff = []

    for key in sorted_keys:
        if key in common_keys:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                node = {
                    "key": key,
                    "type": "nested",
                    "children": build_diff(data1[key], data2[key]),
                }
                diff.append(node)
            elif data1[key] != data2[key]:
                node = {
                    "key": key,
                    "type": "changed",
                    "old_value": data1[key],
                    "new_value": data2[key],
                }
                diff.append(node)
            else:
                node = {"key": key, "type": "unchanged", "value": data1[key]}
                diff.append(node)
        elif key in added_keys:
            node = {"key": key, "type": "added", "value": data2[key]}
            diff.append(node)
        elif key in deleted_keys:
            node = {"key": key, "type": "deleted", "value": data1[key]}
            diff.append(node)

    return diff
