import pylx
from pylx.types import *


def test_main():
    css = [
        Css(
            selector='div.flexbox',
            width=20,
            height=200,
            display=CssDisplayEnum.flex,
            flex_wrap=CssFlexWrapEnum.wrap,
            margin_right=2,
            float=CssFloatEnum.left,
        ),
        Css(
            selector='div.a',
            width=20,
            height=10,
            flex=CssFlexEnum.none,
        )
    ]
    node = Node(
        class_='flexbox',
        children=[
            Node(class_='a'),
        ],
    )

    expect = Node.new(
        class_='flexbox',
        pos=(8, 8, 20, 10),
        children=[
            Node.new(class_='a', pos=(8, 8, 20, 10)),
        ],
    )

    assert pylx.calculate_layout(node, css).model_dump() == expect.model_dump()
