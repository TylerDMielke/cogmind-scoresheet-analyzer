from dataclasses import dataclass


@dataclass
class Bonus:
    bonuses: list[tuple[str, int]]

    @property
    def bonus_score(self) -> int:
        total_bonus_score: int = 0 
        for bonus in self.bonuses:
            total_bonus_score = total_bonus_score + bonus[1]


@dataclass
class Performance:
    evolutions: int
    evolutions_score: int
    regions_visited: int
    regions_visited_score: int
    robots_destroyed: int
    robots_destroyed_score: int
    value_destroyed_score: int
    proto_type_ids: int
    proto_type_ids_score: int
    alien_tech_used: int
    alien_tech_used_score: int
    bonus_score: int

    @property
    def total_score(self):
        return (
            self.evolutions_score 
            + self.regions_visited_score
            + self.robots_destroyed_score
            + self.value_destroyed_score
            + self.proto_type_ids_score
            + self.alien_tech_used_score
            + self.bonus_score
        )


@dataclass
class Cogmind:
    core_integrity: tuple[int, int]
    matter: tuple[int, int]
    energy: tuple[int, int]
    system_corruption: float
    temperature: tuple[str, int]
    movement: tuple[str, int]
    location: tuple[int, str]


@dataclass
class Scoresheet:
    player: str
    result: str
    performance: Performance
    bonus: Bonus
    cogmind: Cogmind
    # TODO: Add the rest of the scoresheet data
