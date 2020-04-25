import json
import pathlib

from tunegen.data import Tune

STATIC_DIR = (pathlib.Path(__file__).parent / "static/").absolute()


def test_converting_tune_to_abc():
    with (STATIC_DIR / "cooleys.json").open() as cooleys_json:
        cooleys_data = json.load(cooleys_json)
    cooleys = Tune(**cooleys_data)

    with (STATIC_DIR / "cooleys.abc").open() as cooleys_abc_file:
        expected_abc = cooleys_abc_file.read()

    assert cooleys.to_abc() == expected_abc
