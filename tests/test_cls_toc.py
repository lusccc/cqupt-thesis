"""Tests for cqupt_thesis.cls — table of contents, list of figures/tables."""
import re

import pytest


class TestTableOfContents:
    def test_toc_title(self, cls_content):
        assert r"\renewcommand\contentsname{目录}" in cls_content

    def test_toc_title_font(self, cls_content):
        assert r"\cfttoctitlefont" in cls_content
        assert r"\zihao{3}" in cls_content

    def test_dotted_leaders(self, cls_content):
        assert r"\renewcommand{\cftchapleader}{\cftdotfill{\cftchapdotsep}}" in cls_content

    def test_dot_sep(self, cls_content):
        assert r"\renewcommand{\cftdotsep}{0.5}" in cls_content

    def test_chapter_before_skip(self, cls_content):
        assert r"\setlength{\cftbeforechapskip}  {0em}" in cls_content

    def test_chapter_page_font_normal(self, cls_content):
        assert r"\renewcommand\cftchappagefont{\normalfont}" in cls_content

    def test_sec_numdepth(self, cls_content):
        assert r"\setcounter{secnumdepth}{3}" in cls_content

    def test_toc_depth(self, cls_content):
        assert r"\setcounter{tocdepth}{2}" in cls_content


class TestListOfFigures:
    def test_lof_title(self, cls_content):
        assert r"\renewcommand\listfigurename{图录}" in cls_content

    def test_lof_title_font(self, cls_content):
        assert r"\cftloftitlefont" in cls_content

    def test_figure_prefix_in_lof(self, cls_content):
        assert r"\renewcommand{\cftfigpresnum}{图}" in cls_content

    def test_figure_num_width(self, cls_content):
        assert r"\setlength{\cftfignumwidth}{3em}" in cls_content


class TestListOfTables:
    def test_lot_title(self, cls_content):
        assert r"\renewcommand\listtablename{表录}" in cls_content

    def test_lot_title_font(self, cls_content):
        assert r"\cftlottitlefont" in cls_content

    def test_table_prefix_in_lot(self, cls_content):
        assert r"\renewcommand{\cfttabpresnum}{表}" in cls_content

    def test_table_num_width(self, cls_content):
        assert r"\setlength{\cfttabnumwidth}{3em}" in cls_content


class TestFigureTableNames:
    def test_figure_name_chinese(self, cls_content):
        assert "figurename = 图" in cls_content

    def test_table_name_chinese(self, cls_content):
        assert "tablename  = 表" in cls_content
