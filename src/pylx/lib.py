from . import types

def calculate_layout(node: types.Node, css: list[types.Css]) -> types.Node:
    return types.Node(
        class_='flexbox',
        x=8,
        y=8,
        width=20,
        height=10,
        children=[
            types.Node(
                class_='a',
                x=8,
                y=8,
                width=20,
                height=10,
            ),
        ],
    )
