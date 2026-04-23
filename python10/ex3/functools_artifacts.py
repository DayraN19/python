from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "max":
        return max(spells)

    if operation == "min":
        return min(spells)

    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
    }

    if operation not in ops:
        return 0

    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "earth": partial(base_enchantment, 50, "earth"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(arg: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatch.register
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatch.register
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    print("Sum:", spell_reducer([10, 20, 30, 40], "add"))
    print("Product:", spell_reducer([10, 20, 30], "multiply"))
    print("Max:", spell_reducer([10, 20, 30, 40], "max"))

    print("\nTesting fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print(memoized_fibonacci.cache_info())

    print("\nTesting dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
