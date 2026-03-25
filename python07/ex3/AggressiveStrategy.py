from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            return ["Enemy Player"]
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        hand.sort(key=lambda card: card.cost)

        played_cards = []
        mana_used = 0

        for card in hand[:2]:
            played_cards.append(card.name)
            mana_used += card.cost

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": played_cards,
                "mana_used": mana_used,
                "targets_attacked": self.prioritize_targets(battlefield),
                "damage_dealt": 8
            }
        }
