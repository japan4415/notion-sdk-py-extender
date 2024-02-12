from pydantic import BaseModel
from enum import Enum
from typing import Optional

from notion_sdk_py_extender.rich_text import RichText
from notion_sdk_py_extender.base import User, Color, Date
from notion_sdk_py_extender.file import File


# https://developers.notion.com/reference/page-property-values


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


class PagePropertiesFormulaType(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    NUMBER = "number"
    STRING = "string"


class PagePropertiesRollupType(str, Enum):
    ARRAY = "array"
    DATE = "date"
    INCOMPLETE = "incomplete"
    NUMBER = "number"
    UNSUPPORTED = "unsupported"


class PagePropertiesRollupFunction(str, Enum):
    AVERAGE = "average"
    CHECKED = "checked"
    COUNT = "count"
    COUNT_PER_GROUP = "count_per_group"
    COUNT_VALUES = "count_values"
    DATE_RANGE = "date_range"
    EARLIEST_DATE = "earliest_date"
    EMPTY = "empty"
    LATEST_DATE = "latest_date"
    MAX = "max"
    MEDIAN = "median"
    MIN = "min"
    NOT_EMPTY = "not_empty"
    PERCENT_CHECKED = "percent_checked"
    PERCENT_EMPTY = "percent_empty"
    PERCENT_NOT_EMPTY = "percent_not_empty"
    PERCENT_PER_GROUP = "percent_per_group"
    PERCENT_UNCHECKED = "percent_unchecked"
    RANGE = "range"
    SHOW_ORIGINAL = "show_original"
    SHOW_UNIQUE = "show_unique"
    SUM = "sum"
    UNCHECKED = "unchecked"
    UNIQUE = "unique"


class PagePropertiesCheckbox(BaseModel):
    checkbox: bool


class PagePropertiesEmail(BaseModel):
    email: str


class PagePropertiesFormula(BaseModel):
    type: PagePropertiesFormulaType
    boolean: Optional[bool] = None
    date: Optional[str] = None
    number: Optional[float] = None
    string: Optional[str] = None


class PagePropertiesMultiSelect(BaseModel):
    id: str
    name: str
    color: Color


class PagePropertiesPhoneNumber(BaseModel):
    phone_number: str


class PagePropertiesRelationPageReference(BaseModel):
    id: str


class PagePropertiesRelation(BaseModel):
    has_more: bool
    relation: list[PagePropertiesRelationPageReference]


class PagePropertiesRollup(BaseModel):
    type: PagePropertiesRollupType
    function: PagePropertiesRollupFunction
    number: Optional[float] = None


class PagePropertiesSelect(BaseModel):
    id: str
    name: str
    color: Color


class PagePropertiesStatus(BaseModel):
    id: str
    name: str
    color: Color


class PagePropertiesTitle(BaseModel):
    id: str
    type: PagePropertiesType
    title: list[RichText]


class PagePropertiesUniqueId(BaseModel):
    number: float
    prefix: Optional[str] = None


class PagePropertiesVerification(BaseModel):
    state: str
    verificated_by: Optional[User] = None
    date: Optional[Date] = None


class PageProperties(BaseModel):
    id: Optional[str] = None
    type: Optional[PagePropertiesType] = None
    checkbox: Optional[PagePropertiesCheckbox] = None
    created_by: Optional[User] = None
    created_time: Optional[str] = None
    date: Optional[Date] = None
    email: Optional[PagePropertiesEmail] = None
    files: Optional[list[File]] = None
    formula: Optional[PagePropertiesFormula] = None
    last_edited_by: Optional[User] = None
    last_edited_time: Optional[str] = None
    multi_select: Optional[list[PagePropertiesMultiSelect]] = None
    number: Optional[float] = None
    people: Optional[list[User]] = None
    phone_number: Optional[PagePropertiesPhoneNumber] = None
    relation: Optional[PagePropertiesRelation] = None
    rollup: Optional[PagePropertiesRollup] = None
    rich_text: Optional[list[RichText]] = None
    select: Optional[PagePropertiesSelect] = None
    status: Optional[PagePropertiesStatus] = None
    title: Optional[PagePropertiesTitle] = None
    url: Optional[str] = None
    unique_id: Optional[PagePropertiesUniqueId] = None
    verification: Optional[PagePropertiesVerification] = None
