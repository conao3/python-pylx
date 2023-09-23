from __future__ import annotations

import enum
from typing import Optional

import pydantic


class CssSizeEnum(enum.Enum):
    px = enum.auto()


class CssDisplayEnum(enum.Enum):
    flex = enum.auto()


class CssFlexWrapEnum(enum.Enum):
    wrap = enum.auto()


class CssFloatEnum(enum.Enum):
    left = enum.auto()


class CssSize(pydantic.BaseModel):
    value: float
    unit: CssSizeEnum = CssSizeEnum.px


class Css(pydantic.BaseModel):
    selector: str
    width: Optional[int | CssSize] = None
    height: Optional[int | CssSize] = None
    display: Optional[CssDisplayEnum] = None
    flex_wrap: Optional[CssFlexWrapEnum] = None
    margin_right: Optional[int | CssSize] = None
    float: Optional[CssFloatEnum] = None
