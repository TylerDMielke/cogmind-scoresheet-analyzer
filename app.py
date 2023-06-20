from pathlib import Path

from textual.app import App, ComposeResult
import textual.widgets as widgets

from cogmind_scoresheet_analyzer.config import APP_NAME, CSS_DIR, DEV_SCORESHEET_DIRECTORY
from cogmind_scoresheet_analyzer.logging_config import get_logger
from cogmind_scoresheet_analyzer.scoresheet import Scoresheet
from cogmind_scoresheet_analyzer.scoresheet_loader import BulkScoresheetLoader
from cogmind_scoresheet_analyzer.scoresheet_screen import ScoresheetScreen

logger = get_logger(APP_NAME)


class CogmindScoresheetAnalyzerApp(App):
    """A Textual app to analyze Cogmind morgue files."""

    def __init__(self):
        super().__init__()
        self.scoresheet_loader: BulkScoresheetLoader = BulkScoresheetLoader(Path(DEV_SCORESHEET_DIRECTORY))

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Close application"),
    ]
    CSS_PATH = str(CSS_DIR / "app.css")
    TITLE = "Cogmind Scoresheet Analyzer"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield widgets.Header()
        yield self._create_scoresheet_list()
        yield widgets.Footer()
    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def on_list_view_selected(self, selected: widgets.ListView.Selected) -> None:
        """Select item currently under cursor."""
        selected_scoresheet: widgets.ListItem = selected.item
        scoresheet: Scoresheet = self.scoresheet_loader.scoresheets[selected_scoresheet.id]
        scoresheet_view: ScoresheetScreen = ScoresheetScreen(scoresheet=scoresheet)
        self.push_screen(scoresheet_view)

    def _create_scoresheet_list(self) -> widgets.ListView:
        items: list[widgets.ListItem] = []
        scoresheets: dict[str, Scoresheet] = self.scoresheet_loader.scoresheets
        for scoresheet_id, scoresheet in scoresheets.items():
            list_item_label: widgets.Label = widgets.Label(f"{scoresheet.player}: {scoresheet.run_date}")
            list_item: widgets.ListItem = widgets.ListItem(list_item_label, id=scoresheet_id)
            items.append(list_item)
        return widgets.ListView(*items)

if __name__ == "__main__":
    app = CogmindScoresheetAnalyzerApp()
    app.run()