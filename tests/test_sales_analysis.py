import pathlib
import tempfile
import pytest
from unittest.mock import mock_open, patch

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_helpers_functions():
    module = run_script(ROOT / "sales_analysis/helpers.py")
    assert module["calculate_total"](2, 3.5) == 7.0
    assert module["format_currency"](1234.5) == "$1,234.50"


def test_analyzer_script_runs_safely():
    import pandas as pd

    df = pd.DataFrame({"product": ["A"], "quantity": [2], "price": [5.0]})
    fake_open = mock_open(read_data="{}")
    patchers = [
        patch("os.path.exists", return_value=True),
        patch("os.makedirs", return_value=None),
        patch("pandas.read_csv", return_value=df),
        patch("pandas.read_json", return_value=df),
        patch("pandas.read_excel", return_value=df),
        patch("json.load", return_value={}),
        patch("builtins.open", fake_open),
        patch("pandas.DataFrame.to_json", return_value=None),
        patch("pandas.DataFrame.to_excel", return_value=None),
        patch("pandas.DataFrame.to_csv", return_value=None),
    ]

    with tempfile.TemporaryDirectory() as tmp:
        module = run_script(
            ROOT / "sales_analysis/analyzer.py",
            cwd=pathlib.Path(tmp),
            patchers=patchers,
        )
        assert module["data_path"] == "data/sales.csv"


def test_analyzer_script_missing_data():
    patchers = [
        patch("os.path.exists", return_value=False),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        with pytest.raises(FileNotFoundError):
            run_script(
                ROOT / "sales_analysis/analyzer.py",
                cwd=pathlib.Path(tmp),
                patchers=patchers,
            )
        # Triggers the else branch


def test_analyzer2_script_runs_safely():
    import pandas as pd

    df = pd.DataFrame({"product": ["A"], "quantity": [3], "price": [10.0]})
    patchers = [patch("pandas.read_csv", return_value=df)]
    with tempfile.TemporaryDirectory() as tmp:
        module = run_script(
            ROOT / "sales_analysis/analyzer2.py",
            cwd=pathlib.Path(tmp),
            extra_syspath=ROOT / "sales_analysis",
            patchers=patchers,
        )
        assert module["grand_total"] == 30.0
