from pathlib import Path
from typing import Optional

from cogmind_scoresheet_analyzer.scoresheet import Scoresheet


class ScoresheetDirNotFoundError(Exception):
    pass


class ScoresheetLoadError(Exception):
    pass


class ScoresheetLoader:
    """Load scoresheets into application."""
    def __init__(self, scoresheet_directory: Optional[str] = None) -> None:
        """Intialize the scoresheet loader."""
        self.scoresheets: list[Scoresheet] = []
        if not scoresheet_directory:
            self._scoresheet_dir = Path("C:\Program Files (x86)\Steam\steamapps\common\Cogmind\scores")
        else:
            self._scoresheet_dir = Path(scoresheet_directory)

    def load_scoresheets(self) -> None:
        if not self._scoresheet_dir.exists():
            raise ScoresheetDirNotFoundError("Could not find scoresheet directory")
        
        for scoresheet in self._scoresheet_dir.glob("*.txt"):
            self._load_scoresheet(scoresheet=scoresheet)
    
    def _load_scoresheet(self, scoresheet: Path) -> Scoresheet:
        with open(scoresheet, "r") as fh:
            import pdb; pdb.set_trace()
            print(fh.read())
