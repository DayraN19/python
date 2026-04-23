def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda x: x['power'], mages))

    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Water Chalice', 'power': 77, 'type': 'accessory'},
        {'name': 'Fire Staff', 'power': 120, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Earth Shield', 'power': 109, 'type': 'armor'}
    ]

    sorted_artifacts = artifact_sorter(artifacts)
    for a in sorted_artifacts:
        print(f"{a['name']} ({a['power']} power)")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting power filter...")
    mages = [
        {'name': 'Aelion', 'power': 50, 'element': 'fire'},
        {'name': 'Lyra', 'power': 90, 'element': 'water'},
        {'name': 'Thorn', 'power': 120, 'element': 'earth'}
    ]

    strong_mages = power_filter(mages, 80)
    for m in strong_mages:
        print(f"{m['name']} ({m['power']} power)")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)
