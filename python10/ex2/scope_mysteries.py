from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulator(value: int) -> int:
        nonlocal total
        total += value
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item: f"{enchantment_type} {item}"


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    a = mage_counter()
    b = mage_counter()
    print(a(), a(), b())

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(acc(20), acc(30))

    print("\nTesting enchantment factory...")
    fire = enchantment_factory("Flaming")
    print(fire("Sword"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print(vault["recall"]("secret"))
    print(vault["recall"]("unknown"))
