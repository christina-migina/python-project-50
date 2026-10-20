from types import NoneType

TYPE_TRANSFORMERS = {
    bool: lambda val: str(val).lower(),
    NoneType: lambda _: 'null',
}

PREFIXES = {
    'unchanged': '    ',
    'added': '  + ',
    'deleted': '  - '
}

INDENT_SIZE = 4 

def make_string(lines, indent):
    formatted = '\n'.join(lines)
    return f"{{\n{formatted}\n{indent}}}"

def make_indent(depth):
    return ' ' * (depth * INDENT_SIZE)

def format_value(value, depth):
    value_type = type(value)
    lines = []
    
    if value_type in TYPE_TRANSFORMERS:
        return TYPE_TRANSFORMERS[value_type](value)
    
    if isinstance(value, dict):
        indent = make_indent(depth)
        item_indent = make_indent(depth + 1)
        lines = []
        for key, value in value.items():
            formatted_value = format_value(value, depth + 1)
            lines.append(f"{item_indent}{key}: {formatted_value}")
        
        return make_string(lines, indent)

    return value

def format_stylish(diff, depth=0):
    formatted_diff = []
    indent = make_indent(depth)

    for node in diff:
        if node['type'] == 'nested':
            children_node = format_stylish(node['children'], depth + 1)
            formatted_diff.append(f"{indent}{PREFIXES['unchanged']}{node['key']}: {children_node}")
        elif node['type'] == 'changed':
            formatted_diff.append(f"{indent}{PREFIXES['deleted']}{node['key']}: {format_value(node['old_value'], depth + 1)}")
            formatted_diff.append(f"{indent}{PREFIXES['added']}{node['key']}: {format_value(node['new_value'], depth + 1)}")
        else:
            formatted_diff.append(f"{indent}{PREFIXES[node['type']]}{node['key']}: {format_value(node['value'], depth + 1)}")

    return make_string(formatted_diff, indent)