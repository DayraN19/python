from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type


    def play(self, game_state: dict) -> dict:
        mana_disponible = game_state.get("available_mana", 0)

        if not self.is_playable(mana_disponible):
            return {"error": "Not enough mana", "playable": False}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Sort type {self.effect_type} is throw !"
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell_name": self.name,
            "type": self.effect_type,
            "targets_hit": targets,
            "status": "Effet magique résolu avec succès"
        }
