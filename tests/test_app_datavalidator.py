import pathlib

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_data_validator_reports_errors():
    module = run_script(ROOT / "app_datavalidator.py")
    validator = module["validator"]
    assert validator.validate_email("bad-email") is False
    assert validator.validate_age(200) is False
    errors = validator.get_errors()
    assert "Invalid email: bad-email" in errors
    assert "Invalid age: 200" in errors
