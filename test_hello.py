import subprocess
import sys
from pathlib import Path

from hello import greet


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"


def test_script_prints_greeting():
    script = Path(__file__).parent / "hello.py"
    result = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, check=True
    )
    assert result.stdout == "Hello, World!\n"
