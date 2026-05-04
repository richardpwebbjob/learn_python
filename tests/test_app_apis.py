import pathlib
from unittest.mock import patch

from tests.test_utils import make_fake_response, run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_app_apis_script_runs_with_mocked_request():
    fake_data = {"current": {"temperature_2m": 25}}
    patchers = [patch("requests.get", return_value=make_fake_response(fake_data))]
    module = run_script(ROOT / "app_apis.py", patchers=patchers)
    assert module["latitude"] == 33.45
    assert module["longitude"] == -112.073891


def test_hello_script_runs_with_mocked_request():
    patchers = [
        patch("requests.get", return_value=make_fake_response({}, status_code=200))
    ]
    module = run_script(ROOT / "hello.py", patchers=patchers)
    assert module["temp"] == 12
