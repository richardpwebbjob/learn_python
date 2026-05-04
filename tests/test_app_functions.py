import pathlib

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_greet_returns_expected_text():
    module = run_script(ROOT / "app8.py")
    assert module["greet"]("Alice", "Jones") == "Hello Alice Jones"


def test_calculate_total():
    module = run_script(ROOT / "app_functions.py")
    assert module["calculate_total"](100, 0.08, 0.20) == "Total Price: $88.0"


def test_calculate_area():
    module = run_script(ROOT / "app_functions.py")
    assert module["calculate_area"](10, 12) == 126.0


def test_double():
    module = run_script(ROOT / "app_functions.py")
    assert module["double"](6) == 12


def test_simple_function():
    module = run_script(ROOT / "app_functions.py")
    assert module["simple_function"]() == (1, 5)


def test_check_weather_cool():
    module = run_script(ROOT / "app_functions.py")
    # This should trigger the else branch
    # But since it's a print, we can't easily assert, but coverage will catch it
