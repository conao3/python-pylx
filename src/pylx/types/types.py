from __future__ import annotations

from typing import Optional

import pydantic


class Node(pydantic.BaseModel):
    tag: str = 'div'
    class_: Optional[str] = None
    children: list[Node] = []

    x: Optional[int] = None
    y: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None

    @classmethod
    def new(
        cls,
        tag: Optional[str] = None,
        class_: Optional[str] = None,
        pos: tuple[Optional[int], Optional[int], Optional[int], Optional[int]] = (None, None, None, None),
        children: list[Node] = []
    ) -> Node:
        return cls.model_validate(
            ({'tag': tag} if tag is not None else {}) |
            ({'class_': class_} if class_ is not None else {}) |
            ({'x': pos[0]} if pos[0] is not None else {}) |
            ({'y': pos[1]} if pos[1] is not None else {}) |
            ({'width': pos[2]} if pos[2] is not None else {}) |
            ({'height': pos[3]} if pos[3] is not None else {}) |
            {'children': children}
        )

    @property
    def left(self) -> Optional[int]:
        return self.x

    @property
    def top(self) -> Optional[int]:
        return self.y

    @property
    def right(self) -> Optional[int]:
        if self.x is None or self.width is None:
            return None

        return self.x + self.width

    @property
    def bottom(self) -> Optional[int]:
        if self.y is None or self.height is None:
            return None

        return self.y + self.height
