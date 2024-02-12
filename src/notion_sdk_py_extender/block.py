from pydantic import BaseModel
from enum import Enum
from typing import Optional

from notion_sdk_py_extender.base import Parent, User, ColorPlusBackground, Date
from notion_sdk_py_extender.rich_text import RichText
from notion_sdk_py_extender.file import File

# https://developers.notion.com/reference/block


class BlockType(str, Enum):
    BOOKMARK = "bookmark"
    BREADCRUMB = "breadcrumb"
    BULLETED_LIST_ITEM = "bulleted_list_item"
    CALLOUT = "callout"
    CHILD_DATABASE = "child_database"
    CHILD_PAGE = "child_page"
    COLUMN = "column"
    COLUMN_LIST = "column_list"
    DIVIDER = "divider"
    EMBED = "embed"
    EQUATION = "equation"
    FILE = "file"
    HEADING_1 = "heading_1"
    HEADING_2 = "heading_2"
    HEADING_3 = "heading_3"
    IMAGE = "image"
    LINK_PREVIEW = "link_preview"
    LINK_TO_PAGE = "link_to_page"
    NUMBERED_LIST_ITEM = "numbered_list_item"
    PARAGRAPH = "paragraph"
    PDF = "pdf"
    QUOTE = "quote"
    SYNCED_BLOCK = "synced_block"
    TABLE = "table"
    TABLE_OF_CONTENTS = "table_of_contents"
    TABLE_ROW = "table_row"
    TEMPLATE = "template"
    TO_DO = "to_do"
    TOGGLE = "toggle"
    UNSUPPORTED = "unsupported"
    VIDEO = "video"


class BlockCodeLanguage(str, Enum):
    ABAP = "abap"
    ARDUINO = "arduino"
    BASH = "bash"
    BASIC = "basic"
    C = "c"
    CLOJURE = "clojure"
    COFFEESCRIPT = "coffeescript"
    C_PLUS_PLUS = "c++"
    C_SHARP = "c#"
    CSS = "css"
    DART = "dart"
    DIFF = "diff"
    DOCKER = "docker"
    ELIXIR = "elixir"
    ELM = "elm"
    ERLANG = "erlang"
    FLOW = "flow"
    FORTRAN = "fortran"
    F_SHARP = "f#"
    GHERKIN = "gherkin"
    GLSL = "glsl"
    GO = "go"
    GRAPHQL = "graphql"
    GROOVY = "groovy"
    HASKELL = "haskell"
    HTML = "html"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    JSON = "json"
    JULIA = "julia"
    KOTLIN = "kotlin"
    LATEX = "latex"
    LESS = "less"
    LISP = "lisp"
    LIVESCRIPT = "livescript"
    LUA = "lua"
    MAKEFILE = "makefile"
    MARKDOWN = "markdown"
    MARKUP = "markup"
    MATLAB = "matlab"
    MERMAID = "mermaid"
    NIX = "nix"
    OBJECTIVE_C = "objective-c"
    OCAML = "ocaml"
    PASCAL = "pascal"
    PERL = "perl"
    PHP = "php"
    PLAIN_TEXT = "plain text"
    POWERSHELL = "powershell"
    PROLOG = "prolog"
    PROTOBUF = "protobuf"
    PYTHON = "python"
    R = "r"
    REASON = "reason"
    RUBY = "ruby"
    RUST = "rust"
    SASS = "sass"
    SCALA = "scala"
    SCHEME = "scheme"
    SCSS = "scss"
    SHELL = "shell"
    SQL = "sql"
    SWIFT = "swift"
    TYPESCRIPT = "typescript"
    VB_NET = "vb.net"
    VERILOG = "verilog"
    VHDL = "vhdl"
    VISUAL_BASIC = "visual basic"
    WEBASSEMBLY = "webassembly"
    XML = "xml"
    YAML = "yaml"
    JAVA_C_CPP_CS = "java/c/c++/c#"


class BlockMentionType(str, Enum):
    DATABASE = "database"
    DATE = "date"
    LINK_PREVIEW = "link_preview"
    PAGE = "page"
    USER = "user"


class BlockBookmark(BaseModel):
    caption: list[RichText]
    url: str


class BlockBreadcrumbBreadcrumb(BaseModel):
    pass


class BlockBreadcrumb(BaseModel):
    type: str
    breadcrumb: BlockBreadcrumbBreadcrumb


class BlockBulletedListItem(BaseModel):
    rich_text: list[RichText]
    color: Optional[ColorPlusBackground] = None
    children: Optional[list] = None


class BlockCallout(BaseModel):
    rich_text: list[RichText]
    icon: str
    color: Optional[ColorPlusBackground] = None


class BlockChildDatabase(BaseModel):
    title: Optional[str] = None


class BlockChildPage(BaseModel):
    title: Optional[str] = None


class BlockCode(BaseModel):
    caption: list[RichText]
    rich_text: list[RichText]
    language: BlockCodeLanguage


class BlockColumn(BaseModel):
    type: str
    column: dict


class BlockColumnList(BaseModel):
    type: Optional[str] = None
    column_list: Optional[dict] = None


class BlockDivider(BaseModel):
    type: str
    divider: dict


class BlockEmbed(BaseModel):
    url: str


class BlockEquation(BaseModel):
    expression: str


class BlockFile(BaseModel):
    caption: list[RichText]
    type: str
    file: File
    name: str


class BlockHeading(BaseModel):
    rich_text: list[RichText]
    color: Optional[ColorPlusBackground] = None
    is_toggleable: Optional[bool] = None


class BlockImageExternal(BaseModel):
    url: str


class BlockImage(BaseModel):
    type: str
    external: BlockImageExternal


class BlockLinkPreview(BaseModel):
    url: str


class BlockMentionDatabase(BaseModel):
    id: str


class BlockMentionLinkPreview(BaseModel):
    url: str


class BlockMentionPage(BaseModel):
    id: str


class BlockMention(BaseModel):
    type: BlockMentionType
    database: Optional[BlockMentionDatabase] = None
    date: Optional[Date] = None
    link_preview: Optional[BlockMentionLinkPreview] = None
    page: Optional[BlockMentionPage] = None
    user: Optional[User] = None


class BlockNumberedListItem(BaseModel):
    rich_text: list[RichText]
    color: Optional[ColorPlusBackground] = None
    children: Optional[list] = None


class BlockParagraph(BaseModel):
    rich_text: list[RichText]
    color: Optional[ColorPlusBackground] = None
    children: Optional[list] = None


class BlockPdf(BaseModel):
    caption: list[RichText]
    type: str
    external: File
    file: File


class BlockQuote(BaseModel):
    rich_text: list[RichText]
    color: Optional[ColorPlusBackground] = None
    children: Optional[list] = None


class BlockSyncedBlockSyncedFrom(BaseModel):
    type: Optional[str] = None
    block_id: Optional[str] = None


class BlockSyncedBlock(BaseModel):
    synced_from: Optional[BlockSyncedBlockSyncedFrom] = None
    children: Optional[list] = None


class BlockTable(BaseModel):
    table_width: int
    has_column_header: bool
    has_row_header: bool


class BlockTableOfContents(BaseModel):
    color: Optional[ColorPlusBackground] = None


class BlockTemplate(BaseModel):
    rich_text: list[RichText]
    children: Optional[list] = None


class BlockToDo(BaseModel):
    rich_text: list[RichText]
    checked: bool
    color: Optional[ColorPlusBackground] = None
    children: Optional[list] = None


class BlockToggle(BaseModel):
    rich_text: list[RichText]
    color: Optional[ColorPlusBackground] = None
    children: Optional[list] = None


class BlockVideoExternal(BaseModel):
    url: str


class BlockVideo(BaseModel):
    type: str
    external: BlockVideoExternal


class Block(BaseModel):
    object: str
    id: str
    type: Optional[BlockType]
    parent: Optional[Parent] = None
    created_time: Optional[str] = None
    created_by: Optional[User] = None
    last_edited_time: Optional[str] = None
    last_edited_by: Optional[User] = None
    archived: Optional[bool] = None
    has_children: Optional[bool] = None
    bookmark: Optional[BlockBookmark] = None
    breadcrumb: Optional[BlockBreadcrumb] = None
    bulleted_list_item: Optional[BlockBulletedListItem] = None
    callout: Optional[BlockCallout] = None
    child_database: Optional[BlockChildDatabase] = None
    child_page: Optional[BlockChildPage] = None
    code: Optional[BlockCode] = None
    column: Optional[BlockColumn] = None
    column_list: Optional[BlockColumnList] = None
    divider: Optional[BlockDivider] = None
    embed: Optional[BlockEmbed] = None
    equation: Optional[BlockEquation] = None
    file: Optional[BlockFile] = None
    heading_1: Optional[BlockHeading] = None
    heading_2: Optional[BlockHeading] = None
    heading_3: Optional[BlockHeading] = None
    image: Optional[BlockImage] = None
    link_preview: Optional[BlockLinkPreview] = None
    mention: Optional[BlockMention] = None
    numbered_list_item: Optional[BlockNumberedListItem] = None
    paragraph: Optional[BlockParagraph] = None
    pdf: Optional[BlockPdf] = None
    quote: Optional[BlockQuote] = None
    synced_block: Optional[BlockSyncedBlock] = None
    table: Optional[BlockTable] = None
    table_of_contents: Optional[BlockTableOfContents] = None
    template: Optional[BlockTemplate] = None
    to_do: Optional[BlockToDo] = None
    toggle: Optional[BlockToggle] = None
    video: Optional[BlockVideo] = None

    def to_update(self):
        return BlockUpdate(
            block_id=self.id,
            parent=self.parent,
            created_time=self.created_time,
            created_by=self.created_by,
            last_edited_time=self.last_edited_time,
            last_edited_by=self.last_edited_by,
            archived=self.archived,
            has_children=self.has_children,
            bookmark=self.bookmark,
            breadcrumb=self.breadcrumb,
            bulleted_list_item=self.bulleted_list_item,
            callout=self.callout,
            child_database=self.child_database,
            child_page=self.child_page,
            code=self.code,
            column=self.column,
            column_list=self.column_list,
            divider=self.divider,
            embed=self.embed,
            equation=self.equation,
            file=self.file,
            heading_1=self.heading_1,
            heading_2=self.heading_2,
            heading_3=self.heading_3,
            image=self.image,
            link_preview=self.link_preview,
            mention=self.mention,
            numbered_list_item=self.numbered_list_item,
            paragraph=self.paragraph,
            pdf=self.pdf,
            quote=self.quote,
            synced_block=self.synced_block,
            table=self.table,
            table_of_contents=self.table_of_contents,
            template=self.template,
            to_do=self.to_do,
            toggle=self.toggle,
            video=self.video,
        )


class BlockUpdate(BaseModel):
    block_id: str
    parent: Optional[Parent] = None
    created_time: Optional[str] = None
    created_by: Optional[User] = None
    last_edited_time: Optional[str] = None
    last_edited_by: Optional[User] = None
    archived: Optional[bool] = None
    has_children: Optional[bool] = None
    bookmark: Optional[BlockBookmark] = None
    breadcrumb: Optional[BlockBreadcrumb] = None
    bulleted_list_item: Optional[BlockBulletedListItem] = None
    callout: Optional[BlockCallout] = None
    child_database: Optional[BlockChildDatabase] = None
    child_page: Optional[BlockChildPage] = None
    code: Optional[BlockCode] = None
    column: Optional[BlockColumn] = None
    column_list: Optional[BlockColumnList] = None
    divider: Optional[BlockDivider] = None
    embed: Optional[BlockEmbed] = None
    equation: Optional[BlockEquation] = None
    file: Optional[BlockFile] = None
    heading_1: Optional[BlockHeading] = None
    heading_2: Optional[BlockHeading] = None
    heading_3: Optional[BlockHeading] = None
    image: Optional[BlockImage] = None
    link_preview: Optional[BlockLinkPreview] = None
    mention: Optional[BlockMention] = None
    numbered_list_item: Optional[BlockNumberedListItem] = None
    paragraph: Optional[BlockParagraph] = None
    pdf: Optional[BlockPdf] = None
    quote: Optional[BlockQuote] = None
    synced_block: Optional[BlockSyncedBlock] = None
    table: Optional[BlockTable] = None
    table_of_contents: Optional[BlockTableOfContents] = None
    template: Optional[BlockTemplate] = None
    to_do: Optional[BlockToDo] = None
    toggle: Optional[BlockToggle] = None
    video: Optional[BlockVideo] = None
