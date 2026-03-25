from .CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        return CreatureCard("Goblin Warrior", 2, "Common", 3, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return ArtifactCard("Mana Ring", 2, "Common", "Mana Boost", 3)

    def create_themed_deck(self, size: int) -> dict:
        deck = [self.create_creature() for _ in range(size)]
        return {"deck_size": len(deck), "theme": "Fantasy"}

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
