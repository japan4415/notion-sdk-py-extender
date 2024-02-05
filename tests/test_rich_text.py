import os
import pytest

def test_make_rich_text_dump_json():
    from notion_sdk_py_extender.rich_text import RichText, RichTextType, RichTextMentionType, RichTextAnnotationsColor, RichTextText, RichTextMentionDatabase, RichTextMentionDate, RichTextMentionLinkPreview, RichTextMentionPage, RichTextMentionTemplateMention, RichTextMentionUser
    rich_text = RichText(
        type=RichTextType.TEXT,
        text=RichTextText(
            content="test",
            link="link"
        )
    )
    assert rich_text.model_dump_json(exclude_none=True) == "{\"type\":\"text\",\"text\":{\"content\":\"test\",\"link\":\"link\"}}"

# def test_read_rich_text_