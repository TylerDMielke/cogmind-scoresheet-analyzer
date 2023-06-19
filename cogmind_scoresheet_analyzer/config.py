"""Configuration values for Cogmind Scoresheet Analyzer."""
from pathlib import Path

APP_NAME: str = "cogmind_scoresheet_analyzer"
FILE_ENCODING: str = "utf-8"
ROOT_DIR: Path = Path(__file__).parent.resolve()
CSS_DIR: Path = Path(ROOT_DIR.parent / "css")

# TODO: Should be removed
DEV_SCORESHEET_DIRECTORY: str = "D:\\SteamLibrary\\steamapps\\common\\Cogmind\\scores"