from .EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")

    hero = EliteCard("Arcane Warrior", 5, "Legendary", 5, 7)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {hero.name} (Elite Card):")

    game_state = {"available_mana": 10}
    print(hero.play(game_state))

    print("\nCombat phase:")
    print(f"Attack result: {hero.attack('Enemy')}")
    print(f"Defense result: {hero.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {hero.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {hero.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
