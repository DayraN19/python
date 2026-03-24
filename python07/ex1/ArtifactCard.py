from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        mana = game_state.get("available_mana", 0)

        if not self.is_playable(mana):
            return {"error": "Not enough mana"}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {"status": "Destroyed"}

        self.durability -= 1

        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability": self.durability
        }
