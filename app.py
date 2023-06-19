from pathlib import Path

from textual.app import App, ComposeResult
import textual.widgets as widgets

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
    TITLE = "Cogmind Scoresheet Analyzer"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield widgets.Header()
        yield self._create_scoresheet_list()
        yield widgets.Footer()
    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def _create_scoresheet_list(self) -> widgets.ListView:
        items: list[widgets.ListItem] = []
        scoresheets: list[Scoresheet] = self.scoresheet_loader.load_scoresheets()
        for scoresheet in scoresheets:
            items.append(widgets.ListItem(widgets.Label(scoresheet.run_date)))
        return widgets.ListView(*items)

if __name__ == "__main__":
    app = CogmindScoresheetAnalyzerApp()
    app.run()