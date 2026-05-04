import os
import pathlib
import pytest
from unittest.mock import patch

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_read_api_key_from_environment():
    patchers = [
        patch("dotenv.load_dotenv", return_value=None),
        patch.dict(
            os.environ,
            {"API_KEY": "test-key", "DATABASE_URL": "sqlite:///test.db"},
            clear=True,
        ),
    ]

    module = run_script(ROOT / "app_readapikey.py", patchers=patchers)
    assert module["api_key"] == "test-key"
    assert module["database"] == "sqlite:///test.db"


def test_read_api_key_missing():
    patchers = [
        patch("dotenv.load_dotenv", return_value=None),
        patch.dict(os.environ, {}, clear=True),
        patch("builtins.print"),  # Suppress print
    ]
    with pytest.raises(KeyError):
        run_script(ROOT / "app_readapikey.py", patchers=patchers)
