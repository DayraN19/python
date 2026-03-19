from ex0.Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super(). __init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, mana_available: int) -> dict:
        playable = mana_available >= self.cost
        if not playable:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }


    def attack_target(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }


    def get_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        }
