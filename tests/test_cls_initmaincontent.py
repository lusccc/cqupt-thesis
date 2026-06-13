"""Tests for cqupt_thesis.cls — \\initmaincontent and main-content control."""
import re

import pytest


class TestInitMainContent:
    def test_initmaincontent_defined(self, cls_content):
        assert r"\newcommand\initmaincontent" in cls_content

    def test_arabic_page_numbering(self, cls_content):
        idx = cls_content.index(r"\newcommand\initmaincontent")
        section = cls_content[idx:idx + 400]
        assert r"\pagenumbering{arabic}" in section

    def test_fancy_pagestyle(self, cls_content):
        idx = cls_content.index(r"\newcommand\initmaincontent")
        section = cls_content[idx:idx + 400]
        assert r"\pagestyle{fancy}" in section

    def test_left_header_university(self, cls_content):
        idx = cls_content.index(r"\newcommand\initmaincontent")
        section = cls_content[idx:idx + 400]
        assert r"\fancyhead[L]" in section
        assert "重庆邮电大学硕士学位论文" in section

    def test_right_header_leftmark(self, cls_content):
        idx = cls_content.index(r"\newcommand\initmaincontent")
        section = cls_content[idx:idx + 400]
        assert r"\leftmark" in section

    def test_maincontent_flag_set(self, cls_content):
        idx = cls_content.index(r"\newcommand\initmaincontent")
        section = cls_content[idx:idx + 400]
        assert r"\maincontenttrue" in section


class TestMainContentFlag:
    def test_newif_defined(self, cls_content):
        assert r"\newif\ifmaincontent" in cls_content

    def test_initially_false(self, cls_content):
        assert r"\maincontentfalse" in cls_content
