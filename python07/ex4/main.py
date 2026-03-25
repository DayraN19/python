from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    plt = TournamentPlatform()

    print("Registering Tournament Cards...")
    c1 = TournamentCard("Fire Dragon", 5, "Rare", "dragon_001")
    c2 = TournamentCard("Ice Wizard", 4, "Rare", "wizard_001")
    plt.register_card(c1)
    plt.register_card(c2)

    for c in [c1, c2]:
        inf = c.get_rank_info()
        print(f"{c.name} (ID: {c.card_id}):\n- Interfaces: "
              f"[Card, Combatable, Rankable]\n- Rating: "
              f"{inf['rating']}\n- Record: {inf['record']}")

    print("\nCreating tournament match...")
    print(f"Match result: {plt.create_match('dragon_001', 'wizard_001')}")

    print("\nTournament Leaderboard:")
    for entry in plt.get_leaderboard():
        print(entry)

    print("\nPlatform Report:")
    print(plt.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
