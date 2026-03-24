from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()

    c = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    s = SpellCard("Lightning Bolt", 3, "Common", "damage")
    a = ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana per turn")

    deck.add_card(c)
    deck.add_card(s)
    deck.add_card(a)

    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("Drawing and playing cards:")

    for _ in range(3):
        card = deck.draw_card()
        if card:
            print(f"Drew: {card.name}"
                  f"({card.__class__.__name__.replace('Card','')})")
            result = card.play({"available_mana": 10})
            print(f"Play result: {result}")

    print("Polymorphism in action: Same interface, different card behaviors !")


if __name__ == "__main__":
    main()
