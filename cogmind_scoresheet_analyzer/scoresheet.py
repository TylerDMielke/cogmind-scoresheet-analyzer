from dataclasses import dataclass
from typing import Optional


@dataclass
class Bonus:
    bonuses: Optional[list[tuple[str, int]]] = None

    @property
    def bonus_score(self) -> int:
        total_bonus_score: int = 0 
        for bonus in self.bonuses:
            total_bonus_score = total_bonus_score + bonus[1]


@dataclass
class Performance:
    evolutions: Optional[int] = None
    evolutions_score: Optional[int] = None
    regions_visited: Optional[int] = None
    regions_visited_score: Optional[int] = None
    robots_destroyed: Optional[int] = None
    robots_destroyed_score: Optional[int] = None
    value_destroyed_score: Optional[int] = None
    prototype_ids: Optional[int] = None
    prototype_ids_score: Optional[int] = None
    alien_tech_used: Optional[int] = None
    alien_tech_used_score: Optional[int] = None
    bonus_score: Optional[int] = None
    total_score: Optional[int] = None


@dataclass
class Cogmind:
    core_integrity: Optional[tuple[int, int]] = None
    matter: Optional[tuple[int, int]] = None
    energy: Optional[tuple[int, int]] = None
    system_corruption: Optional[float] = None
    temperature: Optional[tuple[str, int]] = None
    movement: Optional[tuple[str, int]] = None
    location: Optional[tuple[int, str]] = None


@dataclass
class Scoresheet:
    player: Optional[str] = None
    result: Optional[str] = None
    performance: Optional[Performance] = None
    bonus: Optional[Bonus] = None
    cogmind: Optional[Cogmind] = None
    # TODO: Add the rest of the scoresheet data
