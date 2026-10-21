from types import NoneType

TYPE_TRANSFORMERS = {
    bool: lambda val: str(val).lower(),
    NoneType: lambda _: "null",
    dict: lambda _: "[complex value]",
    str: lambda val: f"'{val}'",
}

TEMPLATES = {
    "added": lambda key, value: (
        f"Property '{key}' was added with value: {value}"
    ),
    "deleted": lambda key: (
        f"Property '{key}' was removed"
    ),
    "changed": lambda key, old_value, new_value: (
        f"Property '{key}' was updated. From {old_value} to {new_value}"
    ),
}


def format_value(value):
    value_type = type(value)

    if value_type in TYPE_TRANSFORMERS:
        return TYPE_TRANSFORMERS[value_type](value)

    return str(value)


def format_plain(diff, path=""):
    formatted_diff = []

    for node in diff:
        current_path = f"{path}.{node['key']}" if path else node["key"]
        if node["type"] == "nested":
            children_node = format_plain(node["children"], current_path)
            if children_node:
                formatted_diff.extend(children_node.split('\n'))
        elif node["type"] == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            line = TEMPLATES["changed"](current_path, old_value, new_value)
            formatted_diff.append(line)
        elif node["type"] == "added":
            value = format_value(node["value"])
            line = TEMPLATES["added"](current_path, value)
            formatted_diff.append(line)
        elif node["type"] == "deleted":
            line = TEMPLATES["deleted"](current_path)
            formatted_diff.append(line)
        
    return '\n'.join(formatted_diff)
