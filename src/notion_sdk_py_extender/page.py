from pydantic import BaseModel
from enum import Enum
from typing import Optional

from notion_sdk_py_extender.rich_text import RichText
from notion_sdk_py_extender.base import User, Parent

# https://developers.notion.com/reference/page


class PagePropertiesType(str, Enum):
    RICH_TEXT = "rich_text"
    NUMBER = "number"
    SELECT = "select"
    MULTI_SELECT = "multi_select"
    STATUS = "status"
    DATE = "date"
    FORMULA = "formula"
    RELATION = "relation"
    ROLLUP = "rollup"
    TITLE = "title"
    PEOPLE = "people"
    FILES = "files"
    CHECKBOX = "checkbox"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    CREATED_TIME = "created_time"
    CREATED_BY = "created_by"
    LAST_EDITED_TIME = "last_edited_time"
    LAST_EDITED_BY = "last_edited_by"


class PageParentType(str, Enum):
    PAGE_ID = "page_id"
    DATABASE_ID = "database_id"
    WORKSPACE = "workspace"
    BLOCK_ID = "block_id"


class PagePropertiesTitle(BaseModel):
    id: str
    type: PagePropertiesType
    title: list[RichText]


class PageProperties(BaseModel):
    title: Optional[PagePropertiesTitle] = None


class PageIcon(BaseModel):
    type: str
    emoji: Optional[str] = None


class Page(BaseModel):
    object: str
    id: str
    created_time: Optional[str] = None
    created_by: Optional[User] = None
    last_edited_time: Optional[str] = None
    last_edited_by: Optional[User] = None
    archived: Optional[bool] = None
    icon: Optional[PageIcon] = None
    cover: Optional[str] = None
    properties: Optional[dict[str, PageProperties]] = None
    parent: Optional[Parent] = None
    url: Optional[str] = None
    public_url: Optional[str] = None
    request_id: Optional[str] = None
