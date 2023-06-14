from io import TextIOWrapper
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
            self.scoresheets.append(self._load_scoresheet(scoresheet_path=scoresheet))
    
    def _load_scoresheet(self, scoresheet_path: Path) -> Scoresheet:
        scoresheet = Scoresheet()

        with open(scoresheet_path, "r") as scoresheet_fh:
            for line in scoresheet_fh:
                if len(line.strip()) == 0:
                    continue
                if "player" in line.lower():
                    scoresheet.player = line[7:].strip()
                elif "result" in line.lower():
                    scoresheet.result = line[7:].strip()
                elif "performance" in line.lower():
                    scoresheet.performance = self._load_performance(scoresheet_filehandle=scoresheet_fh)
                elif "bonus" in line.lower():
                    scoresheet.bonus = self._load_bonus(scoresheet_filehandle=scoresheet_fh)

        return scoresheet

    def _load_performance(self, scoresheet_filehandle: TextIOWrapper) -> Performance:
        performance = Performance()

        for line in scoresheet_filehandle:
            match line.lower().split():
                case ["evolutions", count, score]:
                    performance.evolutions = int(count[1:-1])
                    performance.evolutions_score = int(score)
                case ["regions", "visited", count, score]:
                    performance.regions_visited = int(count[1:-1])
                    performance.regions_visited_score = int(score)
                case ["robots", "destroyed", count, score]:
                    performance.robots_destroyed = int(count[1:-1])
                    performance.robots_destroyed_score = int(score)
                case["value", "destroyed", _, score]:
                    performance.value_destroyed_score = int(score)
                case ["prototype", "ids", count, score]:
                    performance.prototype_ids = int(count[1:-1])
                    performance.prototype_ids_score = int(score)
                case ["alien", "tech", "used", count, score]:
                    performance.alien_tech_used = int(count[1:-1])
                    performance.alien_tech_used_score = int(score)
                case ["bonus", _, score]:
                    performance.bonus_score = int(score)
                case ["total", "score:", score]:
                    performance.total_score = int(score)
                    return performance

    def _load_bonus(self, scoresheet_filehandle: TextIOWrapper) -> Bonus:
        bonus = Bonus()
        bonus.bonuses = []

        for line in scoresheet_filehandle:
            if len(line.strip()) == 0:
                return bonus
            elif "---" in line.strip():
                continue

            split_line: list[str] = line.split()
            bonus_name: str = ""
            bonus_score: Optional[int] = None
            for section in split_line:
                if section.isnumeric():
                    bonus_score = int(section)
                else:
                    bonus_name += section

            bonus.bonuses.append((bonus_name, bonus_score))


    def _load_cogmind(self) -> Cogmind:
        pass
