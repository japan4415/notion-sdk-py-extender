from pydantic import BaseModel
from enum import Enum
from typing import Optional

from notion_sdk_py_extender.base import User, Color, Parent
from notion_sdk_py_extender.rich_text import RichText
from notion_sdk_py_extender.file import File

# https://developers.notion.com/reference/database


class DatabasePropertiesType(str, Enum):
    CHECKBOX = "checkbox"
    CREATED_BY = "created_by"
    CREATED_TIME = "created_time"
    DATE = "date"
    EMAIL = "email"
    FILES = "files"
    FORMULA = "formula"
    LAST_EDITED_BY = "last_edited_by"
    LAST_EDITED_TIME = "last_edited_time"
    MULTI_SELECT = "multi_select"
    NUMBER = "number"
    PEOPLE = "people"
    PHONE_NUMBER = "phone_number"
    RELATION = "relation"
    RICH_TEXT = "rich_text"
    ROLLUP = "rollup"
    SELECT = "select"
    STATUS = "status"
    TITLE = "title"
    URL = "url"


class DatabasePropertiesNumberFormat(str, Enum):
    ARGENTINE_PESO = "argentine_peso"
    BAHT = "baht"
    AUSTRALIAN_DOLLAR = "australian_dollar"
    CANADIAN_DOLLAR = "canadian_dollar"
    CHILEAN_PESO = "chilean_peso"
    COLOMBIAN_PESO = "colombian_peso"
    DANISH_KRONE = "danish_krone"
    DIRHAM = "dirham"
    DOLLAR = "dollar"
    EURO = "euro"
    FORINT = "forint"
    FRANC = "franc"
    HONG_KONG_DOLLAR = "hong_kong_dollar"
    KORUNA = "koruna"
    KRONA = "krona"
    LEU = "leu"
    LIRA = "lira"
    MEXICAN_PESO = "mexican_peso"
    NEW_TAIWAN_DOLLAR = "new_taiwan_dollar"
    NEW_ZEALAND_DOLLAR = "new_zealand_dollar"
    NORWEGIAN_KRONE = "norwegian_krone"
    NUMBER = "number"
    NUMBER_WITH_COMMAS = "number_with_commas"
    PERCENT = "percent"
    PHILIPPINE_PESO = "philippine_peso"
    POUND = "pound"
    PERUVIAN_SOL = "peruvian_sol"
    RAND = "rand"
    REAL = "real"
    RINGGIT = "ringgit"
    RIYAL = "riyal"
    RUBLE = "ruble"
    RUPEE = "rupee"
    RUPIAH = "rupiah"
    SHEKEL = "shekel"
    SINGAPORE_DOLLAR = "singapore_dollar"
    URUGUAYAN_PESO = "uruguayan_peso"
    YEN = "yen"
    YUAN = "yuan"
    WON = "won"
    ZLOTY = "zloty"


class DatabasePropertiesRollupFunction(str, Enum):
    AVERAGE = "average"
    CHECKED = "checked"
    COUNT_PER_GROUP = "count_per_group"
    COUNT = "count"
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
    UNCHECKED = "unchecked"
    UNIQUE = "unique"
    SHOW_ORIGINAL = "show_original"
    SHOW_UNIQUE = "show_unique"
    SUM = "sum"


class DatabasePropertiesFormula(BaseModel):
    expression: Optional[str] = None


class DatabasePropertiesMultiSelect(BaseModel):
    color: Optional[Color] = None
    id: Optional[str] = None
    name: Optional[str] = None


class DatabasePropertiesNumber(BaseModel):
    format: Optional[DatabasePropertiesNumberFormat] = None


class DatabasePropertiesRelation(BaseModel):
    database_id: Optional[str] = None
    synced_property_name: Optional[str] = None
    synced_property_id: Optional[str] = None


class DatabasePropertiesRollup(BaseModel):
    function: Optional[DatabasePropertiesRollupFunction] = None
    relation_property_id: Optional[str] = None
    rollup_property_name: Optional[str] = None
    rollup_property_id: Optional[str] = None
    rollup_property_name: Optional[str] = None


class DatabasePropertiesSelect(BaseModel):
    color: Optional[Color] = None
    id: Optional[str] = None
    name: Optional[str] = None


class DatabasePropertiesStatusOptions(BaseModel):
    color: Optional[Color] = None
    id: Optional[str] = None
    name: Optional[str] = None


class DatabasePropertiesStatusGroups(BaseModel):
    color: Optional[Color] = None
    id: Optional[str] = None
    name: Optional[str] = None
    option_ids: Optional[list[str]] = None


class DatabasePropertiesStatus(BaseModel):
    options: Optional[list[DatabasePropertiesStatusOptions]] = None
    groups: Optional[list[DatabasePropertiesStatusGroups]] = None


class DatabasePropertiesTitle(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    title: Optional[list[RichText]] = None


class DatabaseProperties(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[DatabasePropertiesType] = None
    checkbox: Optional[dict] = None
    created_by: Optional[dict] = None
    created_time: Optional[dict] = None
    date: Optional[dict] = None
    email: Optional[dict] = None
    files: Optional[dict] = None
    formula: Optional[DatabasePropertiesFormula] = None
    last_edited_by: Optional[dict] = None
    last_edited_time: Optional[dict] = None
    multi_select: Optional[list[DatabasePropertiesMultiSelect]] = None
    number: Optional[DatabasePropertiesNumber] = None
    people: Optional[dict] = None
    phone_number: Optional[dict] = None
    relation: Optional[DatabasePropertiesRelation] = None
    rich_text: Optional[dict] = None
    rollup: Optional[DatabasePropertiesRollup] = None
    select: Optional[DatabasePropertiesSelect] = None
    status: Optional[DatabasePropertiesStatus] = None
    title: Optional[list[DatabasePropertiesTitle]] = None
    url: Optional[dict] = None


class Database(BaseModel):
    object: str
    id: str
    created_time: Optional[str] = None
    created_by: Optional[User] = None
    last_edited_time: Optional[str] = None
    last_edited_by: Optional[User] = None
    title: Optional[list[RichText]] = None
    description: Optional[list[RichText]] = None
    icon: Optional[dict] = None
    cover: Optional[File] = None
    properties: Optional[dict[str, DatabaseProperties]] = None
    parent: Optional[Parent] = None
    url: Optional[str] = None
    archived: Optional[bool] = None
    is_inline: Optional[bool] = None
    public_url: Optional[str] = None
