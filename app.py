from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Tab, Tabs

from cogmind_scoresheet_analyzer.config import DEV_SCORESHEET_DIRECTORY
from cogmind_scoresheet_analyzer.scoresheet import Scoresheet
from cogmind_scoresheet_analyzer.scoresheet_loader import BulkScoresheetLoader


class CogmindScoresheetAnalyzerApp(App):
    """A Textual app to analyze Cogmind morgue files."""

    def __init__(self):
        super().__init__()
        self.scoresheet_loader: BulkScoresheetLoader = BulkScoresheetLoader(Path(DEV_SCORESHEET_DIRECTORY))

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Close application"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(name="Cogmind Scoresheet Analyzer")
        yield self._create_tabs()
        yield Footer()
    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_exit_app(self) -> None:
        """Close the application."""

    def _create_tabs(self) -> Tabs:
        tab_list: list[Tab] = []
        scoresheets: list[Scoresheet] = self.scoresheet_loader.load_scoresheets()
        for scoresheet in scoresheets:
            tab_list.append(Tab(scoresheet.run_date))
        return Tabs(*tab_list)

if __name__ == "__main__":
    app = CogmindScoresheetAnalyzerApp()
    app.run()