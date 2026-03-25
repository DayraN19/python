from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.registry: dict[str, TournamentCard] = {}
        self.matches_count: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self.registry[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.registry[card1_id]
        c2 = self.registry[card2_id]
        c1.update_wins(1)
        c2.update_losses(1)
        self.matches_count += 1
        return {
            "winner": card1_id, "loser": card2_id,
            "winner_rating": c1.calculate_rating(),
            "loser_rating": c2.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        cards = []
        for c in self.registry.values():
            cards.append(c)
        n = len(cards)
        for i in range(n):
            for j in range(0, n - i - 1):
                v1 = cards[j].calculate_rating()
                v2 = cards[j + 1].calculate_rating()
                if v1 < v2:
                    cards[j], cards[j + 1] = cards[j + 1], cards[j]
        res = []
        for i in range(len(cards)):
            inf = cards[i].get_rank_info()
            txt = f"{i+1}. {cards[i].name} - Rating: "
            txt += f"{inf['rating']} ({inf['record']})"
            res.append(txt)
        return res

    def generate_tournament_report(self) -> dict:
        total_r = 0
        for c in self.registry.values():
            total_r += c.calculate_rating()
        count = len(self.registry)
        avg = total_r // count if count > 0 else 0
        return {
            "total_cards": count, "matches_played": self.matches_count,
            "avg_rating": avg, "platform_status": "active"
        }
