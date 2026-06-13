"""Tests for cqupt_thesis.cls — appendix, acknowledgements, master's work."""
import re

import pytest

from .conftest import extract_newenvironments


class TestAppendix:
    def test_beginappendix_defined(self, cls_content):
        assert r"\newcommand{\beginappendix}" in cls_content

    def test_appendix_sets_tocdepth(self, cls_content):
        idx = cls_content.index(r"\newcommand{\beginappendix}")
        section = cls_content[idx:idx + 200]
        assert r"\setcounter{tocdepth}{0}" in section


class TestAcknowledgements:
    def test_acknowledgements_env_defined(self, cls_content):
        envs = extract_newenvironments(cls_content)
        assert "acknowledgements" in envs

    def test_acknowledgements_title(self, cls_content):
        idx = cls_content.index(r"\newenvironment{acknowledgements}")
        section = cls_content[idx:idx + 300]
        assert r"\chapter*{致谢}" in section

    def test_acknowledgements_in_toc(self, cls_content):
        idx = cls_content.index(r"\newenvironment{acknowledgements}")
        section = cls_content[idx:idx + 300]
        assert r"\addcontentsline{toc}{chapter}{致谢}" in section

    def test_acknowledgements_mark(self, cls_content):
        idx = cls_content.index(r"\newenvironment{acknowledgements}")
        section = cls_content[idx:idx + 300]
        assert r"\markboth{致谢}{}" in section


class TestMasterMainWork:
    def test_mastermainwork_env_defined(self, cls_content):
        envs = extract_newenvironments(cls_content)
        assert "mastermainwork" in envs

    def test_mastermainwork_title(self, cls_content):
        assert "攻读硕士学位期间从事的科研工作及取得的成果" in cls_content

    def test_mastermainwork_in_toc(self, cls_content):
        idx = cls_content.index(r"\newenvironment{mastermainwork}")
        section = cls_content[idx:idx + 600]
        assert r"\addcontentsline{toc}{chapter}" in section

    def test_mastermainwork_unnumbered_chapters(self, cls_content):
        idx = cls_content.index(r"\newenvironment{mastermainwork}")
        section = cls_content[idx:idx + 600]
        assert "numbering = false" in section


class TestAchievementsList:
    def test_achievements_list_defined(self, cls_content):
        assert r"\newlist{achievements}{enumerate}{1}" in cls_content

    def test_achievements_label_format(self, cls_content):
        assert r"label = [\arabic*]" in cls_content

    def test_achievements_left_margin(self, cls_content):
        assert "leftmargin = 10mm" in cls_content
