from __future__ import annotations

from typing import Optional

import pydantic


class Layout(pydantic.BaseModel):
    x: int
    y: int
    width: int
    height: int

    @property
    def left(self) -> int:
        return self.x

    @property
    def top(self) -> int:
        return self.y

    @property
    def right(self) -> int:
        return self.x + self.width

    @property
    def bottom(self) -> int:
        return self.y + self.height


class Node(pydantic.BaseModel):
    tag: str = 'div'
    class_: Optional[str] = None
    children: list[Node | str] = pydantic.Field(default_factory=list)
