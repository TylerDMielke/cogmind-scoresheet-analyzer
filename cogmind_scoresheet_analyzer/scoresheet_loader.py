from io import TextIOWrapper
from pathlib import Path
from typing import Optional

from cogmind_scoresheet_analyzer.config import APP_NAME
from cogmind_scoresheet_analyzer.exceptions import ScoresheetDirNotFoundError
from cogmind_scoresheet_analyzer.logging_config import get_logger
from cogmind_scoresheet_analyzer.scoresheet import Bonus, Cogmind, Performance, Scoresheet

logger = get_logger(f"{APP_NAME}-{__name__}")


class ScoresheetLoader:
    """Loads in a single scoresheet."""
    def __init__(self, scoresheet_path: Path):
        if not scoresheet_path.exists():
            raise ScoresheetDirNotFoundError(f"Could not find scoresheet at {scoresheet_path}")
        self.scoresheet_path = scoresheet_path

    def load_scoresheet(self) -> Scoresheet:
        scoresheet = Scoresheet()

        with open(self.scoresheet_path, "r") as scoresheet_fh:
            first_line: bool = True  # TODO: Hacky. Find a different way to prevent reading the  first line as a cogmind section.
            for line in scoresheet_fh:
                if first_line:
                    _, date_and_time = line.split("//")
                    scoresheet.run_date = date_and_time
                elif len(line.strip()) == 0:
                    continue
                elif "player" in line.lower():
                    scoresheet.player = line[7:].strip()
                elif "result" in line.lower():
                    scoresheet.result = line[7:].strip()
                elif "performance" in line.lower():
                    scoresheet.performance = self._load_performance(scoresheet_filehandle=scoresheet_fh)
                elif "bonus" in line.lower():
                    scoresheet.bonus = self._load_bonus(scoresheet_filehandle=scoresheet_fh)
                elif "cogmind" in line.lower() and not first_line:
                    scoresheet.cogmind = self._load_cogmind(scoresheet_filehandle=scoresheet_fh)
                first_line = False

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
                case ["value", "destroyed", _, score]:
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

    def _load_cogmind(self, scoresheet_filehandle: TextIOWrapper) -> Cogmind:
        cogmind = Cogmind()

        for line in scoresheet_filehandle:
            match line.lower().split():
                case ["core", "integrity", ratio]:
                    final, maximum = ratio.split("/")
                    cogmind.core_integrity_final = int(final)
                    cogmind.core_integrity_max = int(maximum)
                case ["matter", ratio]:
                    final, maximum = ratio.split("/")
                    cogmind.matter_final = int(final)
                    cogmind.matter_max = int(maximum)
                case ["energy", ratio]:
                    final, maximum = ratio.split("/")
                    cogmind.energy_final = int(final)
                    cogmind.energy_max = int(maximum)
                case ["system", "corruption", percentage]:
                    cogmind.system_corruption = float(percentage[:-1])
                case ["temperature", description, value]:
                    cogmind.temperature_value = int(value[1:-1])
                    cogmind.temperature_description = description
                case ["movement", description, value]:
                    cogmind.movement_value = int(value[1:-1])
                    cogmind.movement_type = description
                case["location", value]:
                    offset, description = value.split("/")
                    cogmind.location_offset = int(offset)
                    cogmind.location_description = description
                    return cogmind


class BulkScoresheetLoader:
    """Load multiple scoresheets into application."""
    def __init__(self, scoresheet_directory: Optional[str] = None) -> None:
        """Initialize the scoresheet loader."""
        if not scoresheet_directory:
            default_path = Path("C:\Program Files (x86)\Steam\steamapps\common\Cogmind\scores")
            logger.debug(f"No path to scoresheets provided. Defaulting to: {default_path}")
            self.scoresheet_directory = default_path
        else:
            logger.debug(f"Searching for scorsheets in: {scoresheet_directory}")
            self.scoresheet_directory = Path(scoresheet_directory)

    def load_scoresheets(self) -> list[Scoresheet]:
        if not self.scoresheet_directory.exists():
            raise ScoresheetDirNotFoundError("Could not find scoresheet directory")

        loaded_scoresheets: list[Scoresheet] = []
        for scoresheet_path in self.scoresheet_directory.glob("*.txt"):
            scoresheet_loader: ScoresheetLoader = ScoresheetLoader(scoresheet_path=scoresheet_path)
            loaded_scoresheets.append(scoresheet_loader.load_scoresheet())

        return loaded_scoresheets
