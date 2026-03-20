from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    
    def play(self, game_state: dict) -> dict:
        mana_disponible = game_state.get("available_mana", 0)

        if not self.is_playable(mana_disponible):
            return {"error": "Not enough mana", "playable": False}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Sort type {self.effect_type} is throw !"
        }

    
    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "status": "Détruit",
                "effect": "Aucun (durabilité épuisée)"
            }

        self.durability -= 1

        return {
            "artifact": self.name,
            "effect_activated": self.effect,
            "remaining_durability": self.durability,
            "status": "Actif" if self.durability > 0 else "S'est brisé après usage"
        }
