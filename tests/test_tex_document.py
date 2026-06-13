"""Tests for thesis.tex — document structure and usage of the template."""
import re

import pytest


class TestDocumentClass:
    def test_uses_cqupt_thesis_class(self, tex_content):
        assert r"\documentclass{cqupt_thesis}" in tex_content

    def test_xelatex_program(self, tex_content):
        assert r"%!TEX program = xelatex" in tex_content


class TestMetadataUsage:
    EXPECTED_COMMANDS = [
        r"\cntitle",
        r"\entitle",
        r"\stuno",
        r"\name{",
        r"\degreeclass",
        r"\major",
        r"\supervisor",
        r"\completedate",
        r"\classifiedindex",
        r"\udc{",
        r"\statesecrets",
        r"\paperno",
        r"\cnkeywords",
        r"\enkeywords",
    ]

    @pytest.mark.parametrize("cmd", EXPECTED_COMMANDS)
    def test_metadata_command_used(self, tex_content, cmd):
        assert cmd in tex_content, f"{cmd} not used in thesis.tex"


class TestDocumentStructure:
    def test_begin_document(self, tex_content):
        assert r"\begin{document}" in tex_content

    def test_end_document(self, tex_content):
        assert r"\end{document}" in tex_content

    def test_makecover(self, tex_content):
        assert r"\makecover" in tex_content

    def test_makestatement(self, tex_content):
        assert r"\makestatement" in tex_content

    def test_cnabstract(self, tex_content):
        assert r"\begin{cnabstract}" in tex_content
        assert r"\end{cnabstract}" in tex_content

    def test_enabstract(self, tex_content):
        assert r"\begin{enabstract}" in tex_content
        assert r"\end{enabstract}" in tex_content

    def test_initmaincontent(self, tex_content):
        assert r"\initmaincontent" in tex_content

    def test_table_of_contents(self, tex_content):
        assert r"\tableofcontents" in tex_content

    def test_list_of_figures(self, tex_content):
        assert r"\listoffigures" in tex_content

    def test_list_of_tables(self, tex_content):
        assert r"\listoftables" in tex_content

    def test_has_chapters(self, tex_content):
        chapters = re.findall(r"\\chapter\{(.+?)\}", tex_content)
        assert len(chapters) >= 1

    def test_has_sections(self, tex_content):
        sections = re.findall(r"\\section\{(.+?)\}", tex_content)
        assert len(sections) >= 1


class TestDocumentOrder:
    """Verify the major structural elements appear in the correct order."""

    def test_cover_before_abstract(self, tex_content):
        assert tex_content.index(r"\makecover") < tex_content.index(r"\begin{cnabstract}")

    def test_statement_before_abstract(self, tex_content):
        assert tex_content.index(r"\makestatement") < tex_content.index(r"\begin{cnabstract}")

    def test_cn_abstract_before_en_abstract(self, tex_content):
        assert tex_content.index(r"\end{cnabstract}") < tex_content.index(r"\begin{enabstract}")

    def test_toc_before_main_content(self, tex_content):
        assert tex_content.index(r"\tableofcontents") < tex_content.index(r"\initmaincontent")

    def test_initmaincontent_before_chapters(self, tex_content):
        first_chapter = re.search(r"\\chapter\{", tex_content)
        assert first_chapter is not None
        assert tex_content.index(r"\initmaincontent") < first_chapter.start()


class TestReferences:
    def test_bibliography_included(self, tex_content):
        assert r"\bibliography{ref}" in tex_content

    def test_reference_environment(self, tex_content):
        assert r"\begin{reference}" in tex_content
        assert r"\end{reference}" in tex_content


class TestBackMatter:
    def test_acknowledgements(self, tex_content):
        assert r"\begin{acknowledgements}" in tex_content
        assert r"\end{acknowledgements}" in tex_content

    def test_master_main_work(self, tex_content):
        assert r"\begin{mastermainwork}" in tex_content
        assert r"\end{mastermainwork}" in tex_content
