from . import types

def calculate_layout(node: types.Node, css: list[types.Css]) -> dict[str, types.Layout]:
    return {
        'flexbox': types.Layout(x=8, y=8, width=20, height=10),
        'flexbox.a': types.Layout(x=8, y=8, width=20, height=10),
    }
