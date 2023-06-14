"""Tests for the ScoresheetLoader Class."""
from pathlib import Path

from cogmind_scoresheet_analyzer.scoresheet import Bonus, Performance, Scoresheet
from cogmind_scoresheet_analyzer.scoresheet_loader import ScoresheetLoader

TEST_SCORESHEET_DIRECTORY: str = "test_data"


def test_scoresheet_load():
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader(scoresheet_directory=TEST_SCORESHEET_DIRECTORY)

    scoresheet_loader.load_scoresheets()
    assert len(scoresheet_loader.scoresheets) == 3

    scoresheet: Scoresheet = scoresheet_loader.scoresheets[0]

    assert scoresheet.player == "Qwze"
    assert scoresheet.result == "Self-destructed"


def test_scoresheet_load_performance():
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader()

    single_score_sheet: Path = Path(f"{TEST_SCORESHEET_DIRECTORY}/Qwze-230611-152311-1-6006.txt")

    with open(single_score_sheet, "r") as fh:
        performance: Performance = scoresheet_loader._load_performance(scoresheet_filehandle=fh)

        assert performance.evolutions == 4
        assert performance.regions_visited == 7
        assert performance.robots_destroyed == 61
        assert performance.prototype_ids == 3
        assert performance.alien_tech_used == 0
        assert performance.total_score == 6006


def test_scoresheet_load_bonus():
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader()

    single_score_sheet: Path = Path(f"{TEST_SCORESHEET_DIRECTORY}/Qwze-230611-152311-1-6006.txt")

    with open(single_score_sheet, "r") as fh:
        _: Performance = scoresheet_loader._load_performance(scoresheet_filehandle=fh)  # TODO: This is lazy. Redo it.
        bonus: Bonus = scoresheet_loader._load_bonus(scoresheet_filehandle=fh)

        assert len(bonus.bonuses) == 2
        assert bonus.bonus_score == 343
