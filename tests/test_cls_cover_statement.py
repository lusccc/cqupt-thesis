"""Tests for cqupt_thesis.cls — cover page and statement page."""
import re

import pytest


class TestCoverPage:
    def test_makecover_defined(self, cls_content):
        assert r"\newcommand{\makecover}" in cls_content

    def test_cover_uses_titlepage(self, cls_content):
        cover_section = cls_content[
            cls_content.index(r"\newcommand{\makecover}"):
            cls_content.index(r"\newcommand{\makestatement}")
        ]
        assert r"\begin{titlepage}" in cover_section
        assert r"\end{titlepage}" in cover_section

    def test_cover_restores_geometry(self, cls_content):
        cover_section = cls_content[
            cls_content.index(r"\newcommand{\makecover}"):
            cls_content.index(r"\newcommand{\makestatement}")
        ]
        assert r"\restoregeometry" in cover_section

    def test_cover_contains_university_name(self, cls_content):
        cover_section = cls_content[
            cls_content.index(r"\newcommand{\makecover}"):
            cls_content.index(r"\newcommand{\makestatement}")
        ]
        assert "重庆邮电大学硕士学位论文" in cover_section

    def test_cover_displays_metadata_fields(self, cls_content):
        cover_section = cls_content[
            cls_content.index(r"\newcommand{\makecover}"):
            cls_content.index(r"\newcommand{\makestatement}")
        ]
        expected_refs = [
            r"\@cntitle",
            r"\@entitle",
            r"\@stuno",
            r"\@name",
            r"\@degreeclass",
            r"\@major",
            r"\@supervisor",
            r"\@completedate",
        ]
        for ref in expected_refs:
            assert ref in cover_section, f"{ref} not referenced on cover page"

    def test_cover_classification_fields(self, cls_content):
        cover_section = cls_content[
            cls_content.index(r"\newcommand{\makecover}"):
            cls_content.index(r"\newcommand{\makestatement}")
        ]
        assert r"\@classifiedindex" in cover_section
        assert r"\@udc" in cover_section
        assert r"\@statesecrets" in cover_section
        assert r"\@paperno" in cover_section

    def test_cover_label_fields(self, cls_content):
        cover_section = cls_content[
            cls_content.index(r"\newcommand{\makecover}"):
            cls_content.index(r"\newcommand{\makestatement}")
        ]
        labels = ["中文题目", "英文题目", "学号", "姓名", "学位类别", "学科专业", "指导教师", "完成日期"]
        for label in labels:
            assert label in cover_section, f"Cover missing label '{label}'"

    def test_cover_optional_subtitles(self, cls_content):
        cover_section = cls_content[
            cls_content.index(r"\newcommand{\makecover}"):
            cls_content.index(r"\newcommand{\makestatement}")
        ]
        assert r"\@cnsubtitle" in cover_section
        assert r"\@ensubtitle" in cover_section


class TestStatementPage:
    def test_makestatement_defined(self, cls_content):
        assert r"\newcommand{\makestatement}" in cls_content

    def test_statement_originality(self, cls_content):
        assert "独" in cls_content and "创" in cls_content and "性" in cls_content

    def test_statement_authorization(self, cls_content):
        assert "学位论文版权使用授权书" in cls_content

    def test_statement_empty_pagestyle(self, cls_content):
        stmt_start = cls_content.index(r"\newcommand{\makestatement}")
        stmt_section = cls_content[stmt_start:stmt_start + 2000]
        assert r"\thispagestyle{empty}" in stmt_section

    def test_statement_signature_fields(self, cls_content):
        assert "作者签名" in cls_content
        assert "导师签名" in cls_content

    def test_statement_restores_geometry(self, cls_content):
        stmt_start = cls_content.index(r"\newcommand{\makestatement}")
        stmt_end = cls_content.index(r"\linespread{1.62}", stmt_start)
        stmt_section = cls_content[stmt_start:stmt_end]
        assert r"\restoregeometry" in stmt_section
