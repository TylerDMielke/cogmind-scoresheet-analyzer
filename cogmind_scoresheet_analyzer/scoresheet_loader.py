from pathlib import Path
from typing import Optional

from cogmind_scoresheet_analyzer.config import APP_NAME
from cogmind_scoresheet_analyzer.logging import get_logger
from cogmind_scoresheet_analyzer.scoresheet import Bonus, Cogmind, Performance, Scoresheet

logger = get_logger(f"{APP_NAME}-{__name__}")


class ScoresheetDirNotFoundError(Exception):
    pass


class ScoresheetLoadError(Exception):
    pass


class ScoresheetLoader:
    """Load scoresheets into application."""
    def __init__(self, scoresheet_directory: Optional[str] = None) -> None:
        """Initialize the scoresheet loader."""
        self.scoresheets: list[Scoresheet] = []
        if not scoresheet_directory:
            default_path = Path("C:\Program Files (x86)\Steam\steamapps\common\Cogmind\scores")
            logger.debug(f"No path to scoresheets provided. Defaulting to: {default_path}")
            self._scoresheet_dir = default_path
        else:
            logger.debug(f"Searching for scorsheets in: {scoresheet_directory}")
            self._scoresheet_dir = Path(scoresheet_directory)

    def load_scoresheets(self) -> None:
        if not self._scoresheet_dir.exists():
            raise ScoresheetDirNotFoundError("Could not find scoresheet directory")
        
        for scoresheet in self._scoresheet_dir.glob("*.txt"):
            self._load_scoresheet(scoresheet=scoresheet)
    
    def _load_scoresheet(self, scoresheet: Path) -> Scoresheet:
        player: Optional[str] = None
        result: Optional[str] = None
        bonus: Optional[Bonus] = None
        cogmind: Optional[Cogmind] = None
        performance: Optional[Performance] = None

        with open(scoresheet, "r") as scoresheet_fh:
            for line in scoresheet_fh:
                if "player" in line.lower():
                    player = line[7:]
                elif "result" in line.lower():
                    result = line[7:]
                else:
                    logger.info(f"No keywords found in: {scoresheet} on line: {line}")

        return Scoresheet(player=player, result=result, bonus=bonus, cogmind=cogmind, performance=performance)
