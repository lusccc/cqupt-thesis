"""Tests for cqupt_thesis.cls — class declaration, options, and base class."""
import re

import pytest


class TestClassDeclaration:
    def test_needs_tex_format(self, cls_content):
        assert r"\NeedsTeXFormat{LaTeX2e}" in cls_content

    def test_provides_class(self, cls_content):
        assert r"\ProvidesClass{cqupt_thesis}" in cls_content

    def test_loads_ctexbook(self, cls_content):
        assert r"\LoadClass" in cls_content
        match = re.search(r"\\LoadClass\[([^\]]+)\]\{(\w+)\}", cls_content)
        assert match is not None
        assert match.group(2) == "ctexbook"

    def test_a4paper_option(self, cls_content):
        match = re.search(r"\\LoadClass\[([^\]]+)\]", cls_content)
        assert match is not None
        options = match.group(1)
        assert "a4paper" in options

    def test_utf8_encoding(self, cls_content):
        match = re.search(r"\\LoadClass\[([^\]]+)\]", cls_content)
        assert match is not None
        assert "UTF8" in match.group(1)

    def test_oneside_mode(self, cls_content):
        match = re.search(r"\\LoadClass\[([^\]]+)\]", cls_content)
        assert match is not None
        assert "oneside" in match.group(1)

    def test_base_font_size(self, cls_content):
        match = re.search(r"\\LoadClass\[([^\]]+)\]", cls_content)
        assert match is not None
        assert "zihao=-4" in match.group(1)

    def test_auto_fake_bold(self, cls_content):
        match = re.search(r"\\LoadClass\[([^\]]+)\]", cls_content)
        assert match is not None
        assert "AutoFakeBold" in match.group(1)

    def test_declare_option_passthrough(self, cls_content):
        assert r"\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexbook}}" in cls_content

    def test_process_options(self, cls_content):
        assert r"\ProcessOptions\relax" in cls_content
