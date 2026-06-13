"""Tests for cqupt_thesis.cls — required packages."""
import pytest

from .conftest import extract_require_packages

EXPECTED_PACKAGES = [
    "float",
    "amssymb",
    "amsmath",
    "amsthm",
    "pifont",
    "notoccite",
    "hyperref",
    "fancyhdr",
    "titletoc",
    "ifthen",
    "graphicx",
    "xcolor",
    "multirow",
    "array",
    "setspace",
    "booktabs",
    "enumitem",
    "pdfpages",
    "geometry",
    "xeCJK",
    "tocloft",
    "unicode-math",
    "etoolbox",
    "listings",
    "algorithm",
    "algorithmicx",
    "algpseudocode",
    "caption",
    "subfigure",
    "footmisc",
    "scrextend",
    "gbt7714",
    "natbib",
    "ragged2e",
]


class TestRequiredPackages:
    @pytest.fixture(autouse=True)
    def _setup(self, cls_content):
        self.packages = extract_require_packages(cls_content)

    @pytest.mark.parametrize("pkg", EXPECTED_PACKAGES)
    def test_package_loaded(self, pkg):
        # Some packages are loaded with options like [subfigure]
        # flatten multi-package loads like {sort&compress}
        flat = []
        for p in self.packages:
            flat.extend(part.strip() for part in p.split(","))
        assert pkg in flat, f"Package '{pkg}' not found in cls file"

    def test_geometry_a4paper_option(self, cls_content):
        assert r"\RequirePackage[a4paper]{geometry}" in cls_content

    def test_hyperref_pdfborder(self, cls_content):
        assert r"\hypersetup{pdfborder=0 0 0}" in cls_content

    def test_tocbibind_nottoc(self, cls_content):
        assert r"\usepackage[nottoc]{tocbibind}" in cls_content

    def test_gbt7714_sort_compress(self, cls_content):
        assert r"\RequirePackage[sort&compress]{gbt7714}" in cls_content

    def test_caption_font_small(self, cls_content):
        assert r"\RequirePackage[font=small,]{caption}" in cls_content

    def test_footmisc_options(self, cls_content):
        assert r"\RequirePackage[bottom,perpage,hang]{footmisc}" in cls_content
