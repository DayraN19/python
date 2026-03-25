from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 card_id: str) -> None:
        super().__init__(name, cost, rarity)
        self.card_id: str = card_id
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = 1200

    def play(self, game_state: dict) -> dict:
        return {"action": f"{self.name} enters tournament"}

    def attack(self, target: str) -> dict:
        return {"attacker": self.name, "target": target, "damage": 5}

    def defend(self, incoming_damage: int) -> dict:
        return {"defender": self.name, "damage_taken": incoming_damage}

    def get_combat_stats(self) -> dict:
        return {"attack": 5, "defense": 5}

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        return {"id": self.card_id, "rank": self.get_rank_info()}
