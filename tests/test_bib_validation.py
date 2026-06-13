"""Tests for ref.bib — bibliography validation."""
import re

import pytest


class TestBibEntries:
    def test_non_empty(self, bib_content):
        assert len(bib_content.strip()) > 0

    def test_has_entries(self, bib_content):
        entries = re.findall(r"@\w+\{", bib_content)
        assert len(entries) >= 1

    def test_entries_have_closing_brace(self, bib_content):
        opens = bib_content.count("{")
        closes = bib_content.count("}")
        assert opens == closes, "Mismatched braces in bib file"

    def test_all_entries_have_type(self, bib_content):
        entries = re.findall(r"@(\w+)\{", bib_content)
        valid_types = {
            "article", "book", "inproceedings", "conference", "incollection",
            "phdthesis", "mastersthesis", "techreport", "manual", "misc",
            "proceedings", "unpublished", "booklet", "inbook", "online",
        }
        for entry_type in entries:
            assert entry_type.lower() in valid_types, (
                f"Unknown bib entry type: @{entry_type}"
            )

    def test_entries_have_keys(self, bib_content):
        entries = re.findall(r"@\w+\{([^,]+),", bib_content)
        assert len(entries) >= 1
        for key in entries:
            assert len(key.strip()) > 0, "Empty bib entry key"

    def test_no_duplicate_keys(self, bib_content):
        keys = re.findall(r"@\w+\{([^,]+),", bib_content)
        keys = [k.strip() for k in keys]
        assert len(keys) == len(set(keys)), "Duplicate bib entry keys found"


class TestBibFields:
    def test_entries_have_title(self, bib_content):
        entries = re.split(r"(?=@\w+\{)", bib_content)
        for entry in entries:
            if entry.strip() and entry.strip().startswith("@"):
                assert re.search(r"title\s*=", entry, re.IGNORECASE), (
                    f"Bib entry missing title field: {entry[:80]}..."
                )

    def test_article_has_journal(self, bib_content):
        entries = re.split(r"(?=@\w+\{)", bib_content)
        for entry in entries:
            if entry.strip().lower().startswith("@article"):
                assert re.search(r"journal\s*=", entry, re.IGNORECASE), (
                    f"Article entry missing journal: {entry[:80]}..."
                )
