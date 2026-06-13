"""Shared fixtures for LaTeX template tests."""
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
CLS_PATH = ROOT / "cqupt_thesis.cls"
TEX_PATH = ROOT / "thesis.tex"
BIB_PATH = ROOT / "ref.bib"


@pytest.fixture(scope="session")
def cls_content() -> str:
    return CLS_PATH.read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def tex_content() -> str:
    return TEX_PATH.read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def bib_content() -> str:
    return BIB_PATH.read_text(encoding="utf-8")


def extract_newcommands(text: str) -> list[str]:
    """Return command names defined via \\newcommand or \\renewcommand."""
    pattern = r"\\(?:new|renew)command\{?\\(\w+)\}?"
    return re.findall(pattern, text)


def extract_newenvironments(text: str) -> list[str]:
    """Return environment names defined via \\newenvironment."""
    pattern = r"\\newenvironment\{(\w+)\}"
    return re.findall(pattern, text)


def extract_require_packages(text: str) -> list[str]:
    """Return package names loaded via \\RequirePackage or \\usepackage."""
    pattern = r"\\(?:RequirePackage|usepackage)(?:\[[^\]]*\])?\{([^}]+)\}"
    return re.findall(pattern, text)
