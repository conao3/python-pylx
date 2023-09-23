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
    ]
    node = Node(
        class_='flexbox',
        children=[
            Node(class_='a'),
        ],
    )

    expect = {
        'flexbox': Layout(x=8, y=8, width=20, height=10),
        'flexbox.a': Layout(x=8, y=8, width=20, height=10),
    }

    assert pylx.calculate_layout(node, css) == expect
