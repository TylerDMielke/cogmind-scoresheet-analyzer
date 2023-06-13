from pathlib import Path
from typing import Optional

from src.scoresheet import Scoresheet


class ScoresheetDirNotFoundError(Exception):
    pass


class ScoresheetLoadError(Exception):
    pass


class ScoresheetLoader:
    """Load scoresheets into application."""
    scoresheets: list[Scoresheet]
    _scoresheet_dir: Path

    def __init__(self, scoresheet_directory: Optional[str]) -> None:
        """Intialize the scoresheet loader."""
        if not scoresheet_directory:
            self._scoresheet_dir = "C:\Program Files (x86)\Steam\steamapps\common\Cogmind\scores"
        else:
            self._scoresheet_dir = scoresheet_directory

    def load_scoresheets(self) -> None:
        if not self._scoresheet_dir.exists():
            raise ScoresheetDirNotFoundError("Could not find scoresheet directory")
        
        for scoresheet in self._scoresheet_dir.glob("*.txt"):
            with open(scoresheet, "r") as fh:
                print(fh.read())
