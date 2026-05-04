import os
import runpy
import sys
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import MagicMock

ROOT = Path(__file__).resolve().parents[1]


def make_fake_response(json_data, status_code=200):
    fake = MagicMock()
    fake.json.return_value = json_data
    fake.status_code = status_code
    return fake


def run_script(script_path, cwd=None, extra_syspath=None, patchers=None):
    script_path = Path(script_path)
    old_cwd = os.getcwd()
    old_path = sys.path.copy()
    if cwd is None:
        cwd = ROOT
    try:
        os.chdir(str(cwd))
        if extra_syspath:
            sys.path.insert(0, str(extra_syspath))
        with ExitStack() as stack:
            for patcher in patchers or []:
                stack.enter_context(patcher)
            return runpy.run_path(str(script_path), init_globals={})
    finally:
        os.chdir(old_cwd)
        sys.path[:] = old_path
