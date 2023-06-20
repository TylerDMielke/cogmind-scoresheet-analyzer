from textual import widgets
from textual.app import ComposeResult, Screen
from textual.containers import Center, Container

from cogmind_scoresheet_analyzer.scoresheet import Bonus, Cogmind, Performance, Scoresheet


class ScoresheetScreen(Screen):
    def __init__(self, scoresheet: Scoresheet):
        super().__init__()
        self.scoresheet = scoresheet

    BINDINGS = [
        ("q", "dismiss", "Go Back"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield widgets.Header()
        yield Center(
            widgets.Label(f"Played by: {self.scoresheet.player} on {self.scoresheet.run_date}"),
        )
        yield widgets.Label(f"Result: {self.scoresheet.result}")
        yield self._performance_section()
        yield self._bonus_section()
        yield self._cogmind_section()
        yield widgets.Footer()

    def _performance_section(self) -> Container:
        performance: Performance = self.scoresheet.performance

        performance_labels: list[widgets.Label] = []
        for field_name, field_value in performance.__dict__.items():
            performance_labels.append(widgets.Label(f"{field_name}: {field_value}"))

        container: Container = Container(
            *performance_labels,
            id="performance_container"
        )
        container.border_title = "Performance"

        return container

    def _bonus_section(self) -> Container:
        bonus: Bonus = self.scoresheet.bonus
        bonuses: list[tuple[str, int]] = bonus.bonuses

        bonus_labels: list[widgets.Label] = []
        for bonus_name, bonus_value in bonuses:
            bonus_labels.append(widgets.Label(f"{bonus_name}: {bonus_value}"))

        container: Container = Container(
            *bonus_labels,
            id="bonus_container"
        )
        container.border_title = "Bonus"

        return container

    def _cogmind_section(self) -> Container:
        cogmind: Cogmind = self.scoresheet.cogmind

        cogmind_labels: list[widgets.Label] = []
        for field_name, field_value in cogmind.__dict__.items():
            cogmind_labels.append(widgets.Label(f"{field_name}: {field_value}"))

        container: Container = Container(
            *cogmind_labels,
            id="cogmind_container"
        )
        container.border_title = "Cogmind"

        return container
