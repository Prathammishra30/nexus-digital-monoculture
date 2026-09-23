"""Unit Tests for Manifest Parsers.

Verifies parser interface instantiation and base contract compliance.
"""

import sys
from pathlib import Path

# Ensure engine folders are in Python path
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(root_dir / "discovery-engine"))
sys.path.insert(0, str(root_dir / "risk-engine"))
sys.path.insert(0, str(root_dir / "graph"))
sys.path.insert(0, str(root_dir))

from parsers.npm_parser import NPMParser
from parsers.python_parser import PythonParser
from parsers.go_parser import GoParser
from parsers.docker_parser import DockerParser
from parsers.terraform_parser import TerraformParser


def test_parser_instantiation():
    """Verify all ecosystem parser classes instantiate cleanly."""
    npm = NPMParser()
    python = PythonParser()
    go = GoParser()
    docker = DockerParser()
    tf = TerraformParser()

    assert npm is not None
    assert python is not None
    assert go is not None
    assert docker is not None
    assert tf is not None


def test_npm_parser_contract():
    """Verify NPM parser handles empty content without crashing."""
    parser = NPMParser()
    result = parser.parse_package_json("{}")
    assert isinstance(result, list)


def test_python_parser_contract():
    """Verify Python parser handles empty requirements text."""
    parser = PythonParser()
    result = parser.parse_requirements_txt("")
    assert isinstance(result, list)
