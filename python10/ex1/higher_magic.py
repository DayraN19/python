from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Combine deux sorts en un seul.
    Accepte n'importe quel nombre d'arguments via *args et **kwargs.
    """
    def combined_spell(*args: Any, **kwargs: Any) -> tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Amplifie la puissance du sort.
    Multiplie le premier argument reçu par le multiplicateur.
    """
    def amplified_spell(*args: Any, **kwargs: Any) -> Any:
        # On convertit args en liste pour pouvoir modifier la valeur
        args_list = list(args)
        if args_list:
            args_list[0] = args_list[0] * multiplier
        return base_spell(*args_list, **kwargs)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Lance le sort uniquement si la condition est True.
    """
    def conditional_spell(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    Lance une liste de sorts à la suite avec les mêmes arguments.
    """
    def sequence_spell(*args: Any, **kwargs: Any) -> list[Any]:
        return [s(*args, **kwargs) for s in spells]
    return sequence_spell


# --- Zone de Test (Main) ---
if __name__ == "__main__":
    # 1. Test avec deux arguments (Target, Power)
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    # 2. Test avec un seul argument (Power) - Simulation de ton erreur Runtime
    def simple_damage(power: int) -> int:
        return power * 2

    print("--- Testing Higher Realm ---")

    # Test Combiner (Flexible)
    combined = spell_combiner(simple_damage, lambda p: p + 10)
    print(f"Test combined(5): {combined(5)}")  # Devrait renvoyer (10, 15)

    # Test Amplifier
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Amplified fireball: {mega_fireball('Dragon', 10)}")

    # Test Sequence
    multi_cast = spell_sequence([fireball, heal])
    print(f"Sequence results: {multi_cast('Orc', 50)}")
