import pathlib

from tests.test_utils import run_script

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_api_config_defaults():
    module = run_script(ROOT / "app_apiconfig.py")
    APIConfig = module["APIConfig"]
    config = APIConfig("sk-test-key")
    assert config.model == "gpt-3.5-turbo"
    assert config.max_tokens == 100
    assert config.base_url == "https://api.openai.com/v1"
