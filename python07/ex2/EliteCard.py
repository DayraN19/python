from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, mana_capacity: int,
                 effect: str = "Unleashes ancient power") -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense_value = 3
        self.mana_capacity = mana_capacity
        self.current_mana = mana_capacity
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

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(incoming_damage, self.defense_value)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True if self.mana_capacity > 0 else False
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense_value
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_capacity": self.mana_capacity,
            "current_mana": self.current_mana
        }

    def channel_mana(self, amount: int) -> dict:
        self.current_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.current_mana
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        cost = 4
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": cost
        }
