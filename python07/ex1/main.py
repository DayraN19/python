import ArtifactCard, SpellCard
my_deck = [
    SpellCard("Boule de Feu", 3, "Rare", "Dommage"),
    ArtifactCard("Anneau de Mana", 2, "Epic", 5, "Gain Mana")
]

for carte in my_deck:
    resultat = carte.play(mon_game_state)
    print(resultat)