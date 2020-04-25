"""Objects for scraping/parsing tunes on http://thesession.org."""


import re
from typing import Dict

import bs4
import requests

from .tune import Tune

__all__ = ("TuneParser",)


class TuneParser:
    """
    Class for parsing tunes encoded in HTML on http://thesession.org.

    Args:
        session_id: The integer specified at the end of the tune url
            e.g https://thesession.org/tunes/12701,.
    """

    base_url = "http://thesession.org/tunes"
    field_id_to_name = {
        "X": "setting",
        "T": "title",
        "R": "tunetype",
        "M": "meter",
        "L": "unit_note_length",
        "K": "key",
    }

    def __init__(self, session_id: int) -> None:
        self.session_id = session_id
        self.abc = self._get_abc()

    def _get_abc(self) -> str:
        tune_page_html = requests.get(f"{self.base_url}/{self.session_id}").text
        soup = bs4.BeautifulSoup(tune_page_html)
        sheet_music_div = soup.find(attrs={"id": "sheetmusic1"})
        abc = sheet_music_div.find(attrs={"name": "abc"}).attrs["value"]
        return abc

    def parse(self) -> Tune:
        tune_args = self._parse_metadata()
        tune_args["notes"] = self._parse_notes()
        tune_args["session_id"] = self.session_id
        return Tune(**tune_args)

    def _parse_metadata(self) -> Dict[str, str]:
        metadata_pattern = re.compile(r"(\w): (.+?)\n")
        metadata = {}
        for field_id, field_value in metadata_pattern.findall(self.abc):
            field_name = self.field_id_to_name[field_id]
            metadata[field_name] = field_value
        return metadata

    def _parse_notes(self) -> str:
        notes_pattern = re.compile(r"(\w: .+?\n)+(.+)", flags=re.DOTALL)
        notes = notes_pattern.match(self.abc).group(2)
        return notes
