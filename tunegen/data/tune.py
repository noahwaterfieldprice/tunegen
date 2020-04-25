"""Container objects for storing tune data."""

import enum
from dataclasses import dataclass

__all__ = ("Tune", "TuneType")


class TuneType(enum.Enum):
    REEL = "reel"
    JIG = "jig"


@dataclass
class Tune:
    session_id: int
    setting: int
    title: str
    tunetype: TuneType
    meter: str
    unit_note_length: str
    key: str
    notes: str
