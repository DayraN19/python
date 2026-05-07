from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditioned_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditioned_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence_spell


if __name__ == "__main__":
    test_values = [14, 18, 15]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_strong(target: str, power: int) -> bool:
        return power > 20
    print("Testing Higher Realm...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined: {combined(test_targets[0], test_values[0])}")
    amp = power_amplifier(fireball, 2)
    print(f"Amplified: {amp(test_targets[1], test_values[1])}")
    cond = conditional_caster(is_strong, fireball)
    print(f"Conditional(Low): {cond(test_targets[2], test_values[2])}")
    strong_amp = power_amplifier(fireball, 3)
    cond_strong = conditional_caster(is_strong, strong_amp)
    print(f"Conditional(High): {cond_strong(test_targets[2], test_values[2])}")
    seq = spell_sequence([fireball, heal])
    print(f"Sequence: {seq(test_targets[3], test_values[0])}")
