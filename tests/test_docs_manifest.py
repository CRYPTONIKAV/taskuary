"""The docs footer version must track releases (issue #134)."""

import datetime
import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_version_matches_pyproject():
    manifest = json.loads((ROOT / "docs/site/manifest.json").read_text())
    with open(ROOT / "pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    assert manifest["version"] == pyproject["project"]["version"], (
        manifest["version"],
        pyproject["project"]["version"],
    )


def test_manifest_updated_is_a_date():
    manifest = json.loads((ROOT / "docs/site/manifest.json").read_text())
    datetime.date.fromisoformat(manifest["updated"])
