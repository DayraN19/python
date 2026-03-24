from ex0.CreatureCard import CreatureCard

card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

print(" === DataDeck Card Foundation ===\n")
print(" Testing Abstract Base Class design:\n")
print("CreatureCard Info:")
print(card.get_info())

print("\nPlaying Fire Dragon with 6 mana available:")
print(f"Playable: {6 >= card.cost}")
print(f"Play result: {card.play({'available_mana': 6})}")

print("\nFire Dragon attacks Goblin Warrior:")
print(f"Attack result: {card.attack_target('Goblin Warrior')}")

print("\nTesting insufficient mana (3 available):")
print(f"Playable: {3 >= card.cost}\n")

print("Abstract pattern successfully demonstrated!")
