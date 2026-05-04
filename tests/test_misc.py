import pathlib
from unittest.mock import mock_open, patch

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_app_apikey_empty_module_runs():
    module = run_script(ROOT / "app_apikey.py")
    assert isinstance(module, dict)


def test_app_errorhandling_with_open_mock():
    fake_file = mock_open(read_data="sample data")
    patchers = [patch("builtins.open", fake_file)]
    module = run_script(ROOT / "app_errorhandling.py", patchers=patchers)
    assert isinstance(module, dict)
