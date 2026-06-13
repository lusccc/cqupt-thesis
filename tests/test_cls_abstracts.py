"""Tests for cqupt_thesis.cls — abstract environments."""
import re

import pytest

from .conftest import extract_newenvironments


class TestChineseAbstract:
    def test_cnabstract_environment_defined(self, cls_content):
        envs = extract_newenvironments(cls_content)
        assert "cnabstract" in envs

    def test_cnabstract_roman_page_numbering(self, cls_content):
        idx = cls_content.index(r"\newenvironment{cnabstract}")
        section = cls_content[idx:idx + 600]
        assert r"\pagenumbering{Roman}" in section

    def test_cnabstract_header(self, cls_content):
        idx = cls_content.index(r"\newenvironment{cnabstract}")
        section = cls_content[idx:idx + 600]
        assert r"\makefancyhf{摘要}" in section

    def test_cnabstract_title(self, cls_content):
        idx = cls_content.index(r"\newenvironment{cnabstract}")
        section = cls_content[idx:idx + 600]
        assert "摘要" in section

    def test_cnabstract_outputs_keywords(self, cls_content):
        idx = cls_content.index(r"\newenvironment{cnabstract}")
        section = cls_content[idx:idx + 800]
        assert "关键词" in section
        assert r"\@cnkeywords" in section


class TestEnglishAbstract:
    def test_enabstract_environment_defined(self, cls_content):
        envs = extract_newenvironments(cls_content)
        assert "enabstract" in envs

    def test_enabstract_header(self, cls_content):
        idx = cls_content.index(r"\newenvironment{enabstract}")
        section = cls_content[idx:idx + 600]
        assert r"\makefancyhf{Abstract}" in section

    def test_enabstract_chapter_star(self, cls_content):
        idx = cls_content.index(r"\newenvironment{enabstract}")
        section = cls_content[idx:idx + 600]
        assert r"\chapter*{Abstract}" in section

    def test_enabstract_linespread(self, cls_content):
        idx = cls_content.index(r"\newenvironment{enabstract}")
        section = cls_content[idx:idx + 600]
        assert r"\linespread{1.44}" in section

    def test_enabstract_outputs_keywords(self, cls_content):
        idx = cls_content.index(r"\newenvironment{enabstract}")
        end_idx = cls_content.index(r"% ------开始设置 目录样式")
        section = cls_content[idx:end_idx]
        assert "Keywords" in section
        assert r"\@enkeywords" in section
