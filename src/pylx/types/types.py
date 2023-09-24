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

    def set(self, x: Optional[int], y: Optional[int], width: Optional[int], height: Optional[int]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

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
