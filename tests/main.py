import os
from pprint import pprint
from notion_client import Client
from notion_sdk_py_extender.rich_text import (
    RichText,
    RichTextType,
    RichTextMentionType,
    RichTextAnnotationsColor,
    RichTextText,
    RichTextMentionDatabase,
    RichTextMentionDate,
    RichTextMentionLinkPreview,
    RichTextMentionPage,
    RichTextMentionTemplateMention,
    RichTextMentionUser,
)
from notion_sdk_py_extender.page import Page
from notion_sdk_py_extender.block import Block
from notion_sdk_py_extender.database import Database

token = os.environ.get("NOTION_SDK_PY_EXTENDER_TOKEN")
page_id = os.environ.get("NOTION_SDK_PY_EXTENDER_PAGE_ID")
database_id = "d7cdeac02c2340819fa327d10984da65"

if __name__ == "__main__":
    c = Client(auth=token)
    # r = c.pages.retrieve(
    #     **{
    #         "page_id": page_id,
    #     }
    # )
    # pprint(r)
    # page = Page(**r)
    # pprint(page)
    # page.properties.title.title[0].text.content = "notion-sdk-py-extender"
    # pprint(page.properties.model_dump(exclude_none=True))
    # c.pages.update(
    #     **{
    #         "page_id": page.id,
    #         "properties": page.properties.model_dump(exclude_none=True),
    #     }
    # )
    # r = c.blocks.children.list(**{"block_id": page_id, "page_size": 50})
    # pprint(r)
    # for block in r["results"]:
    #     # pprint(block)
    #     a = Block(**block)
    #     pprint(a)
    # r = c.databases.retrieve(
    #     **{
    #         "database_id": database_id,
    #     }
    # )
    # pprint(r)
    # database = Database(**r)
    # pprint(database)
    r = c.databases.query(
        **{
            "database_id": database_id,
        }
    )
    # pprint(r)
    for database in r["results"]:
        pprint(database)
        a = Page(**database)
        pprint(a)
