import json
import pathlib

from tunegen.data import Tune, TuneParser

STATIC_DIR = (pathlib.Path(__file__).parent / "static/").absolute()


def test_parsing_tune():
    with (STATIC_DIR / "cooleys.json").open() as cooleys_json:
        expected_tune_data = json.load(cooleys_json)
    expected_tune = Tune(**expected_tune_data)

    parser = TuneParser(session_id=1)
    parsed_tune = parser.parse()

    assert parsed_tune == expected_tune
