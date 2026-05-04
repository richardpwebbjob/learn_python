import pathlib

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_app_imports_script_executes():
    module = run_script(ROOT / "app_imports.py")
    assert "current_dir" in module
    assert "choice" in module
    assert "number" in module
