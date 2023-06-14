"""Tests for the ScoresheetLoader Class."""
from cogmind_scoresheet_analyzer.scoresheet import Scoresheet
from cogmind_scoresheet_analyzer.scoresheet_loader import ScoresheetLoader

TEST_SCORESHEET_DIRECTORY: str = "test_data"


def test_scoresheet_load():
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader(scoresheet_directory=TEST_SCORESHEET_DIRECTORY)

    scoresheet_loader.load_scoresheets()
    assert len(scoresheet_loader.scoresheets) == 3

    scoresheet: Scoresheet = scoresheet_loader.scoresheets[0]

    assert scoresheet.player == "Qwze"