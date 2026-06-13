"""Tests for cqupt_thesis.cls — page geometry, headers, footers."""
import re

import pytest


class TestPageGeometry:
    def test_newgeometry_margins(self, cls_content):
        pattern = r"\\newgeometry\{([^}]+)\}"
        matches = re.findall(pattern, cls_content)
        assert len(matches) >= 1
        main_geom = matches[0]
        assert "left=3.5cm" in main_geom
        assert "right=2.45cm" in main_geom
        assert "top=3cm" in main_geom
        assert "bottom=2.4cm" in main_geom

    def test_headheight(self, cls_content):
        match = re.search(r"\\newgeometry\{([^}]+)\}", cls_content)
        assert match is not None
        assert "headheight=1.5cm" in match.group(1)


class TestHeaderFooter:
    def test_fancy_pagestyle(self, cls_content):
        assert r"\pagestyle{fancy}" in cls_content

    def test_headrulewidth(self, cls_content):
        assert r"\renewcommand\headrulewidth{0.8pt}" in cls_content

    def test_makefancyhf_defined(self, cls_content):
        assert r"\newcommand{\makefancyhf}" in cls_content

    def test_makefancyhf_university_header(self, cls_content):
        assert "重庆邮电大学硕士学位论文" in cls_content

    def test_makefancyhf_page_number_footer(self, cls_content):
        assert r"\fancyfoot[CO,CE]{\zihao{-5}\thepage}" in cls_content


class TestFontSettings:
    def test_times_new_roman(self, cls_content):
        assert r"\setmainfont{Times New Roman}" in cls_content

    def test_simsun_main(self, cls_content):
        assert "SimSun" in cls_content

    def test_consolas_mono(self, cls_content):
        assert r"\setmonofont[Mapping=tex-text]{Consolas}" in cls_content

    def test_linespread_body(self, cls_content):
        assert r"\linespread{1.62}\selectfont" in cls_content

    def test_linespread_cover(self, cls_content):
        assert r"\linespread{1.5}\selectfont" in cls_content

    def test_cuheiti_defined(self, cls_content):
        assert r"\newCJKfontfamily\cuheiti{heiti}" in cls_content

    def test_cusongti_defined(self, cls_content):
        assert r"\newCJKfontfamily\cusongti{SimSun}" in cls_content

    def test_punctstyle(self, cls_content):
        assert r"\punctstyle{hangmobanjiao}" in cls_content
