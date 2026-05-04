import pathlib

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_dog_initialization():
    module = run_script(ROOT / "app_classes.py")
    Dog = module["Dog"]
    dog = Dog("Buddy", "Beagle")
    assert dog.name == "Buddy"
    assert dog.breed == "Beagle"
