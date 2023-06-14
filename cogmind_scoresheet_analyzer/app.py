from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.widgets._header import HeaderTitle


class CogmindScoresheetAnalyzerApp(App):
    """A Textual app to analyze Cogmind morgue files."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = CogmindScoresheetAnalyzerApp()
    app.run()