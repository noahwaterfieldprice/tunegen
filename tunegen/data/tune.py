"""Container objects for storing tune data."""

import enum
from dataclasses import dataclass

__all__ = ("ABC_FIELD_ID_NAMES", "Tune", "TuneType")

ABC_FIELD_ID_NAMES = {
    "X": "setting",
    "T": "title",
    "R": "tunetype",
    "M": "meter",
    "L": "unit_note_length",
    "K": "key",
}


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

    def to_abc(self) -> str:
        abc_metadata = []
        for field_id, field_name in ABC_FIELD_ID_NAMES.items():
            abc_metadata.append(f"{field_id}: {getattr(self, field_name)}")
        abc_metadata.append(self.notes)
        return "\n".join(abc_metadata)
