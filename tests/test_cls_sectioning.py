"""Tests for cqupt_thesis.cls — chapter/section/subsection formatting via ctexset."""
import re

import pytest


class TestChapterFormat:
    def test_chapter_pagestyle_fancy(self, cls_content):
        assert "pagestyle={fancy}" in cls_content

    def test_chapter_font_size(self, cls_content):
        idx = cls_content.index("chapter= {")
        section = cls_content[idx:idx + 300]
        assert r"\zihao{3}" in section

    def test_chapter_heiti_bold(self, cls_content):
        idx = cls_content.index("chapter= {")
        section = cls_content[idx:idx + 300]
        assert r"\heiti" in section
        assert r"\bfseries" in section

    def test_chapter_arabic_numbering(self, cls_content):
        idx = cls_content.index("chapter= {")
        section = cls_content[idx:idx + 300]
        assert r"number={\arabic{chapter}}" in section

    def test_chapter_fixskip(self, cls_content):
        idx = cls_content.index("chapter= {")
        section = cls_content[idx:idx + 400]
        assert "fixskip=true" in section


class TestSectionFormat:
    def test_section_font_size(self, cls_content):
        idx = cls_content.index("section={")
        section = cls_content[idx:idx + 300]
        assert r"\zihao{-3}" in section

    def test_section_heiti_bold(self, cls_content):
        idx = cls_content.index("section={")
        section = cls_content[idx:idx + 300]
        assert r"\heiti" in section
        assert r"\bfseries" in section

    def test_section_flushleft(self, cls_content):
        idx = cls_content.index("section={")
        section = cls_content[idx:idx + 300]
        assert r"\flushleft" in section


class TestSubsectionFormat:
    def test_subsection_font_size(self, cls_content):
        idx = cls_content.index("subsection={")
        section = cls_content[idx:idx + 300]
        assert r"\zihao{4}" in section

    def test_subsection_heiti(self, cls_content):
        idx = cls_content.index("subsection={")
        section = cls_content[idx:idx + 300]
        assert r"\heiti" in section


class TestSubsubsectionFormat:
    def test_subsubsection_cusongti_bold(self, cls_content):
        idx = cls_content.index("subsubsection={")
        section = cls_content[idx:idx + 300]
        assert r"\cusongti" in section
        assert r"\bfseries" in section
