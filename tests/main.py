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
database_id = "8537d5731ea340e89fb5e7ca780239f9"

if __name__ == "__main__":
    c = Client(auth=token)
    r = c.pages.retrieve(
        **{
            "page_id": page_id,
        }
    )
    page_update = Page(**r).to_update()
    page_update.properties["title"].title[0].text.content = "notion-sdk-py-extend"
    c.pages.update(**page_update.model_dump(exclude_none=True))
    r = c.blocks.children.list(**{"block_id": page_id, "page_size": 50})
    for block in r["results"]:
        b = Block(**block)
        if b.type == "paragraph" and len(b.paragraph.rich_text) != 0:
            b.paragraph.rich_text[0].text.content = "notion-sdk-py-extend"
            c.blocks.update(**b.to_update().model_dump(exclude_none=True))
    r = c.databases.retrieve(
        **{
            "database_id": database_id,
        }
    )
    pprint(r)
    database = Database(**r)
    # pprint(database)
    # r = c.databases.query(
    #     **{
    #         "database_id": database_id,
    #     }
    # )
    # # pprint(r)
    # for database in r["results"]:
    #     pprint(database)
    #     a = Page(**database)
    #     pprint(a)
