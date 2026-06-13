"""Tests for cqupt_thesis.cls — figure/table formatting, captions, algorithms."""
import re

import pytest


class TestCaptionSetup:
    def test_table_caption_labelsep(self, cls_content):
        # Skip commented-out captionsetup lines
        pattern = r"(?<!%)\\captionsetup\[table\]\{([^}]+)\}"
        import re
        matches = re.findall(pattern, cls_content)
        assert any("labelsep=space" in m for m in matches)

    def test_figure_caption_labelsep(self, cls_content):
        assert r"\captionsetup[figure]{" in cls_content
        idx = cls_content.index(r"\captionsetup[figure]{")
        section = cls_content[idx:idx + 200]
        assert "labelsep=space" in section

    def test_table_font_size_in_maincontent(self, cls_content):
        assert r"\zihao{5}" in cls_content

    def test_figure_font_size(self, cls_content):
        assert r"\AtBeginEnvironment{figure}{\zihao{5}}" in cls_content


class TestColumnTypes:
    def test_ragged_right_column_P(self, cls_content):
        assert r"\newcolumntype{P}" in cls_content

    def test_centered_column_x(self, cls_content):
        assert r"\newcolumntype{x}" in cls_content


class TestCommentTable:
    def test_makecommenttable_defined(self, cls_content):
        assert r"\newcommand\makecommenttable" in cls_content

    def test_commenttable_header(self, cls_content):
        idx = cls_content.index(r"\newcommand\makecommenttable")
        section = cls_content[idx:idx + 500]
        assert r"\makefancyhf{注释表}" in section

    def test_commenttable_adds_to_toc(self, cls_content):
        idx = cls_content.index(r"\newcommand\makecommenttable")
        section = cls_content[idx:idx + 500]
        assert r"\addcontentsline{toc}{chapter}{注释表}" in section


class TestAlgorithm:
    def test_algorithm_float_name(self, cls_content):
        assert r"\floatname{algorithm}{算法}" in cls_content

    def test_algorithm_input_label(self, cls_content):
        assert r"\renewcommand{\algorithmicrequire}{\textbf{输入:}}" in cls_content

    def test_algorithm_output_label(self, cls_content):
        assert r"\renewcommand{\algorithmicensure}{\textbf{输出:}}" in cls_content
