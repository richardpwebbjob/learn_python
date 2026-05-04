import pathlib
import tempfile
from unittest.mock import patch

from tests.test_utils import make_fake_response, run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_app_data_script_runs_with_mocked_io():
    fake_data = {
        "daily": {
            "time": ["2026-05-01", "2026-05-02"],
            "temperature_2m_max": [20, 22],
            "temperature_2m_min": [10, 11],
        }
    }
    patchers = [
        patch("requests.get", return_value=make_fake_response(fake_data)),
        patch("matplotlib.pyplot.savefig", return_value=None),
        patch("matplotlib.pyplot.show", return_value=None),
        patch("pandas.DataFrame.to_csv", return_value=None),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        module = run_script(
            ROOT / "app_data.py", cwd=pathlib.Path(tmp), patchers=patchers
        )
        assert "url" in module
