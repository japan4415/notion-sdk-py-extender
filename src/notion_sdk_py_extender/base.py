from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Color(str, Enum):
    BLUE = "blue"
    BROWN = "brown"
    DEFAULT = "default"
    GRAY = "gray"
    GREEN = "green"
    ORANGE = "orange"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    YELLOW = "yellow"


class ColorPlusBackground(str, Enum):
    BLUE = "blue"
    BLUE_BACKGROUND = "blue_background"
    BROWN = "brown"
    BROWN_BACKGROUND = "brown_background"
    DEFAULT = "default"
    GRAY = "gray"
    GRAY_BACKGROUND = "gray_background"
    GREEN = "green"
    GREEN_BACKGROUND = "green_background"
    ORANGE = "orange"
    ORANGE_BACKGROUND = "orange_background"
    PINK = "pink"
    PINK_BACKGROUND = "pink_background"
    PURPLE = "purple"
    PURPLE_BACKGROUND = "purple_background"
    RED = "red"
    RED_BACKGROUND = "red_background"
    YELLOW = "yellow"
    YELLOW_BACKGROUND = "yellow_background"


class User(BaseModel):
    object: str
    id: str


class Date(BaseModel):
    end: Optional[str] = None
    start: Optional[str] = None


class Parent(BaseModel):
    type: str
    database_id: Optional[str] = None
    page_id: Optional[str] = None
    workspace: Optional[bool] = None
    block_id: Optional[str] = None
