from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_count: int = 0
        self.total_damage: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured"}

        hand = [
            self.factory.create_creature(),
            self.factory.create_spell()
        ]

        battlefield = ["Enemy Player", "Enemy Creature"]
        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.turns_count += 1
        self.total_damage += turn_result["actions"]["damage_dealt"]

        return turn_result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_count,
            "strategy_used":
                self.strategy.get_strategy_name() if self.strategy else "None",
            "total_damage": self.total_damage,
            "cards_created": 3
        }
