def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {'first_kill', 'level_10',
                       'treasure_hunter', 'speed_demon'}
    bob: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set[str] = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===\n")

    all_achievements: set[str] = alice | bob | charlie
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all: set[str] = alice & bob & charlie
    print(f"Common to all players: {common_all}\n")

    rare_achievements: set[str] = {ach for ach in all_achievements if
                                   (ach in alice) + (ach in bob) +
                                   (ach in charlie) == 1}
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    ft_achievement_tracker()
