"""Tests for the ScoresheetLoader Class."""
from pathlib import Path

from cogmind_scoresheet_analyzer.scoresheet import Bonus, Cogmind, Performance, Scoresheet
from cogmind_scoresheet_analyzer.scoresheet_loader import BulkScoresheetLoader, ScoresheetLoader

TEST_SCORESHEET_DIRECTORY: str = "test_data"
TEST_SCORESHEET: str = "Qwze-230611-152311-1-6006.txt"


def test_scoresheet_load_player_result():
    scoresheet_path: Path = Path(f"{TEST_SCORESHEET_DIRECTORY}/{TEST_SCORESHEET}")
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader(scoresheet_path=scoresheet_path)

    scoresheet: Scoresheet = scoresheet_loader.load_scoresheet()
    assert scoresheet.player == "Qwze"
    assert scoresheet.result == "Self-destructed"


def test_scoresheet_load_performance():
    scoresheet_path: Path = Path(f"{TEST_SCORESHEET_DIRECTORY}/{TEST_SCORESHEET}")
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader(scoresheet_path=scoresheet_path)

    scoresheet: Scoresheet = scoresheet_loader.load_scoresheet()
    performance: Performance = scoresheet.performance
    assert performance.evolutions == 4
    assert performance.regions_visited == 7
    assert performance.robots_destroyed == 61
    assert performance.prototype_ids == 3
    assert performance.alien_tech_used == 0
    assert performance.total_score == 6006


def test_scoresheet_load_bonus():
    scoresheet_path: Path = Path(f"{TEST_SCORESHEET_DIRECTORY}/{TEST_SCORESHEET}")
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader(scoresheet_path=scoresheet_path)

    scoresheet: Scoresheet = scoresheet_loader.load_scoresheet()
    bonus: Bonus = scoresheet.bonus
    assert len(bonus.bonuses) == 2
    assert bonus.bonus_score == 343


def test_scoresheet_load_cogmind():
    scoresheet_path: Path = Path(f"{TEST_SCORESHEET_DIRECTORY}/{TEST_SCORESHEET}")
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader(scoresheet_path=scoresheet_path)

    scoresheet: Scoresheet = scoresheet_loader.load_scoresheet()
    cogmind: Cogmind = scoresheet.cogmind
    assert cogmind.core_integrity_final == 709
    assert cogmind.core_integrity_max == 850
    assert cogmind.matter_final == 55
    assert cogmind.matter_max == 300
    assert cogmind.energy_final == 100
    assert cogmind.energy_max == 100
    assert cogmind.system_corruption == 0.0
    assert cogmind.temperature_description == "cool"
    assert cogmind.temperature_value == 0
    assert cogmind.movement_type == "core"
    assert cogmind.movement_value == 50
    assert cogmind.location_offset == -6
    assert cogmind.location_description == "factory"


def test_bulk_scoresheet_load():
    scoresheet_directory: Path = Path(TEST_SCORESHEET_DIRECTORY)
    bulk_scoresheet_loader: BulkScoresheetLoader = BulkScoresheetLoader(scoresheet_directory=scoresheet_directory)

    loaded_scoresheets: list[Scoresheet] = bulk_scoresheet_loader.load_scoresheets()
    assert len(loaded_scoresheets)
    for scoresheet in loaded_scoresheets:
        assert scoresheet.player == "Qwze"
