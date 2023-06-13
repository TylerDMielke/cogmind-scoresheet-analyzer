"""Tests for the ScoresheetLoader Class."""
from scoresheet import Scoresheet
from scoresheet_loader import ScoresheetLoader

TEST_SCORESHEET_DIRECTORY: str = "test_data"


def test_scoresheet_load():
    scoresheet_loader: ScoresheetLoader = ScoresheetLoader(scoresheet_directory=TEST_SCORESHEET_DIRECTORY)

    assert len(scoresheet_loader.scoresheets) == 3

    scoresheet: Scoresheet = scoresheet_loader.scoresheets[0]

    assert scoresheet.player == "Qwze"