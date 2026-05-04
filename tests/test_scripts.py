import pathlib
import tempfile

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_simple_assignment_scripts():
    paths = [
        ROOT / "app.py",
        ROOT / "app2.py",
        ROOT / "app3.py",
        ROOT / "app4.py",
        ROOT / "app5.py",
        ROOT / "app6.py",
        ROOT / "app7.py",
        ROOT / "app9.py",
        ROOT / "app10.py",
        ROOT / "app11.py",
        ROOT / "app12.py",
        ROOT / "main.py",
    ]
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)
        for script_path in paths:
            result = run_script(script_path, cwd=tmp_path)
            assert isinstance(result, dict)
