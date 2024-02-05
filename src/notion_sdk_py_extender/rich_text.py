from pydantic import BaseModel
from enum import Enum
from typing import Optional

# https://developers.notion.com/reference/rich-text

class RichTextType(str, Enum):
    TEXT = "text"
    MENTION = "mention"
    EQUATION = "equation"

class RichTextMentionType(str, Enum):
    DATABASE = "database"
    DATE = "date"
    LINK_PREVIEW = "link_preview"
    PAGE = "page"
    TEMPLATE_MENTION = "template"
    USER = "user"

class RichTextAnnotationsColor(str, Enum):
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

class RichTextText(BaseModel):
    content: str
    link: Optional[str]

class RichTextMentionDatabase(BaseModel):
    id: str

class RichTextMentionDate(BaseModel):
    start: str
    end: str

class RichTextMentionLinkPreview(BaseModel):
    url: str

class RichTextMentionPage(BaseModel):
    id: str

class RichTextMentionTemplateMention(BaseModel):
    type: str

class RichTextMentionUser(BaseModel):
    id: str

class RichTextMention(BaseModel):
    type: RichTextMentionType
    database: RichTextMentionDatabase
    date: RichTextMentionDate
    link_preview: RichTextMentionLinkPreview
    page: RichTextMentionPage
    template_mention: RichTextMentionTemplateMention
    user: RichTextMentionUser

class RichTextEquation(BaseModel):
    expression: str

class RichTextAnnotations(BaseModel):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: RichTextAnnotationsColor

class RichText(BaseModel):
    type: RichTextType
    text: Optional[RichTextText] = None
    mention: Optional[RichTextMention] = None
    equation: Optional[RichTextEquation] = None
    annotations: Optional[RichTextAnnotations] = None
    plain_text: Optional[str] = None
    href: Optional[str] = None