"""Tests for cqupt_thesis.cls — math/theorem environments."""
import re

import pytest

THEOREM_ENVS = {
    "proof": "证明:",
    "assumption": "假设",
    "definition": "定义",
    "proposition": "命题",
    "lemma": "引理",
    "theorem": "定理",
    "axiom": "公理",
    "corollary": "推论",
    "exercise": "练习",
    "example": "例",
    "remark": "注释",
    "problem": "问题",
    "conjecture": "猜想",
}


class TestTheoremEnvironments:
    @pytest.mark.parametrize("env,label", THEOREM_ENVS.items())
    def test_theorem_env_defined(self, cls_content, env, label):
        if env == "proof":
            assert rf"\newtheorem*{{proof}}{{{label}}}" in cls_content
        else:
            pattern = rf"\\newtheorem\{{{env}\}}\{{{label}\}}"
            assert re.search(pattern, cls_content), (
                f"Theorem environment '{env}' with label '{label}' not found"
            )

    @pytest.mark.parametrize(
        "env",
        ["assumption", "definition", "proposition", "lemma", "theorem",
         "axiom", "corollary", "exercise", "example", "remark", "problem", "conjecture"],
    )
    def test_theorem_numbered_by_chapter(self, cls_content, env):
        pattern = rf"\\newtheorem\{{{env}\}}\{{[^}}]+\}}\[chapter\]"
        assert re.search(pattern, cls_content), (
            f"Theorem '{env}' not numbered by chapter"
        )


class TestTheoremStyle:
    def test_custom_theorem_style_defined(self, cls_content):
        assert r"\newtheoremstyle{theoremdd}" in cls_content

    def test_theorem_style_applied(self, cls_content):
        assert r"\theoremstyle{theoremdd}" in cls_content

    def test_theorem_body_normalfont(self, cls_content):
        idx = cls_content.index(r"\newtheoremstyle{theoremdd}")
        section = cls_content[idx:idx + 400]
        assert r"{\normalfont}" in section

    def test_theorem_head_bold(self, cls_content):
        idx = cls_content.index(r"\newtheoremstyle{theoremdd}")
        section = cls_content[idx:idx + 400]
        assert r"{\bfseries}" in section


class TestDisplayMathSpacing:
    def test_above_display_skip(self, cls_content):
        assert r"\setlength{\abovedisplayskip}     {3pt}" in cls_content

    def test_below_display_skip(self, cls_content):
        assert r"\setlength{\belowdisplayskip}     {3pt}" in cls_content

    def test_above_display_short_skip(self, cls_content):
        assert r"\setlength{\abovedisplayshortskip}{3pt}" in cls_content

    def test_below_display_short_skip(self, cls_content):
        assert r"\setlength{\belowdisplayshortskip}{3pt}" in cls_content
