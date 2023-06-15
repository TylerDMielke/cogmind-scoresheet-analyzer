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
        return total_bonus_score


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
    core_integrity_final: Optional[int] = None
    core_integrity_max: Optional[int] = None
    matter_final: Optional[int] = None
    matter_max: Optional[int] = None
    energy_final: Optional[int] = None
    energy_max: Optional[int] = None
    system_corruption: Optional[float] = None
    temperature_description: Optional[str] = None
    temperature_value: Optional[int] = None
    movement_type: Optional[str] = None
    movement_value: Optional[int] = None
    location_offset: Optional[int] = None
    location_description: Optional[str] = None


@dataclass
class Scoresheet:
    run_date: Optional[str] = None  # TODO: Should this be a Datetime?
    player: Optional[str] = None
    result: Optional[str] = None
    performance: Optional[Performance] = None
    bonus: Optional[Bonus] = None
    cogmind: Optional[Cogmind] = None
    # TODO: Add the rest of the scoresheet data
