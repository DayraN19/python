from ex0.Card import Card
import random
class Deck():
    def __init__(self) -> None:
        # On crée une liste vide qui stockera nos instances de cartes
        self.cards: list[Card] = []
    def add_card(self, card: Card) -> None:
        # Ajoute l'objet carte à la liste
        self.cards.append(card)


    def remove_card(self, card_name: str) -> bool:
        # Cherche la carte par son nom et la retire
        # Retourne True si trouvé et supprimé, False sinon
        pass


    def shuffle(self) -> None:
        # Utilise le module random pour mélanger self.cards
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        # Retire la dernière carte de la liste et la renvoie
        # Utilise .pop()
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        # Calcule le nombre total, le coût moyen, 
        # et compte combien de types différents (Creature, Spell, etc.)
        # Retourne un dictionnaire avec ces infos
        pass


    for card in my_deck: card.play()