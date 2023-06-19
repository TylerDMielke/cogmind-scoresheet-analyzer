from textual.app import ComposeResult, Screen
from textual.widgets import Footer, Header, Label

from cogmind_scoresheet_analyzer.scoresheet import Scoresheet


class ScoresheetScreen(Screen):
    def __init__(self, scoresheet: Scoresheet):
        super().__init__()
        self.scoresheet = scoresheet

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "dismiss", "Go Back"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Label(f"Played by: {self.scoresheet.player}: {self.scoresheet.run_date}", id="scoresheet_header")
        yield Label(f"Result: {self.scoresheet.result}", id="result")
        yield Footer()