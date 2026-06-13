"""Tests for cqupt_thesis.cls — document metadata commands."""
import re

import pytest

from .conftest import extract_newcommands

METADATA_COMMANDS = [
    "classifiedindex",
    "udc",
    "paperno",
    "statesecrets",
    "cntitle",
    "cnsubtitle",
    "cnsubsubtitle",
    "entitle",
    "ensubtitle",
    "ensubsubtitle",
    "stuno",
    "name",
    "degreeclass",
    "major",
    "supervisor",
    "completedate",
    "cnkeywords",
    "enkeywords",
]

INTERNAL_VARS = [
    "@classifiedindex",
    "@udc",
    "@statesecrets",
    "@paperno",
    "@cntitle",
    "@cnsubtitle",
    "@cnsubsubtitle",
    "@entitle",
    "@ensubtitle",
    "@ensubsubtitle",
    "@stuno",
    "@name",
    "@degreeclass",
    "@major",
    "@supervisor",
    "@completedate",
    "@cnkeywords",
    "@enkeywords",
]


class TestMetadataCommands:
    @pytest.fixture(autouse=True)
    def _setup(self, cls_content):
        self.commands = extract_newcommands(cls_content)
        self.content = cls_content

    @pytest.mark.parametrize("cmd", METADATA_COMMANDS)
    def test_metadata_command_defined(self, cmd):
        assert cmd in self.commands, f"Metadata command \\{cmd} not defined"

    @pytest.mark.parametrize("var", INTERNAL_VARS)
    def test_internal_variable_initialized(self, var):
        # Internal vars are initialized via \newcommand\@varname{}
        escaped = var.replace("@", r"@")
        pattern = rf"\\newcommand\\{escaped}\{{\}}"
        assert re.search(pattern, self.content), (
            f"Internal variable \\{var} not initialized"
        )

    def test_metadata_commands_use_renewcommand(self):
        for cmd in METADATA_COMMANDS:
            pattern = rf"\\newcommand\\{cmd}\[1\]\{{\\renewcommand"
            assert re.search(pattern, self.content), (
                f"\\{cmd} does not use \\renewcommand pattern"
            )

    def test_metadata_count(self):
        count = sum(1 for cmd in METADATA_COMMANDS if cmd in self.commands)
        assert count == len(METADATA_COMMANDS)
