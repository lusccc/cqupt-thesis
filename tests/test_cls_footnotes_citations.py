"""Tests for cqupt_thesis.cls — footnotes, citations, bibliography."""
import re

import pytest


class TestFootnotes:
    def test_circled_footnote_helper(self, cls_content):
        assert r"\newcommand\thu@circled" in cls_content

    def test_footnote_ding_symbol(self, cls_content):
        assert r"\renewcommand{\thefootnote}" in cls_content
        assert r"\ding{\numexpr171+\value{footnote}}" in cls_content

    def test_footnote_separator_rule(self, cls_content):
        assert r"\def\footnoterule" in cls_content

    def test_footnote_sep_length(self, cls_content):
        assert r"\setlength{\footnotesep}{16pt}" in cls_content

    def test_footnote_font_size(self, cls_content):
        assert r"\zihao{6}" in cls_content

    def test_footnote_max_check(self, cls_content):
        assert r"\ifnum#1 >10" in cls_content


class TestCitations:
    def test_incite_command_defined(self, cls_content):
        assert r"\DeclareRobustCommand*{\incite}" in cls_content

    def test_incite_uses_cite(self, cls_content):
        idx = cls_content.index(r"\DeclareRobustCommand*{\incite}")
        section = cls_content[idx:idx + 300]
        assert r"\cite{#1}" in section

    def test_incite_sets_numeric_style(self, cls_content):
        idx = cls_content.index(r"\DeclareRobustCommand*{\incite}")
        section = cls_content[idx:idx + 300]
        assert r"\setcitestyle{numbers}" in section


class TestBibliography:
    def test_bibliography_style(self, cls_content):
        assert r"\bibliographystyle{gbt7714-numerical}" in cls_content

    def test_bibsep_zero(self, cls_content):
        assert r"\setlength{\bibsep}{0pt}" in cls_content

    def test_reference_environment(self, cls_content):
        from .conftest import extract_newenvironments
        envs = extract_newenvironments(cls_content)
        assert "reference" in envs

    def test_reference_font_size(self, cls_content):
        idx = cls_content.index(r"\newenvironment{reference}")
        section = cls_content[idx:idx + 300]
        assert r"\zihao{5}" in section
