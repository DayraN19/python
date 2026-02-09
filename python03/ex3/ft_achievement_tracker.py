def ft_achievement_tracker():

    print("=== Achievement Tracking System ===")
    print("")
    mouss = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_master",
        "I.C"
    }

    sylv1 = {
        "first_kill",
        "level_10",
        "boss_lady",
        "collector"
    }

    matte = {
        "level_10",
        "treasure_hunter",
        "boss_lady",
        "speed_master",
        "perfectionist"
    }

    print("Mouss Achievement:", mouss)
    print("Sylv1 Achievement:", sylv1)
    print("Matte Achievement:", matte)
    print("")
    print("=== Achievement Analytics ===")
    all_achievements = mouss.union(sylv1).union(matte)
    print("All Single Achievement:", all_achievements)
    print("Number of Achivement:", len(all_achievements))
    print("")
    common_achievement = mouss.intersection(sylv1).intersection(matte)
    print("Common to all players:", common_achievement)

    mouss_only = mouss.difference(sylv1).difference(matte)
    sylv1_only = sylv1.difference(mouss).difference(matte)
    matte_only = matte.difference(mouss).difference(sylv1)

    rare_achievement = mouss_only.union(sylv1_only).union(matte_only)
    print("Rare Achievement", rare_achievement)
    print("")
    mouss_sylv1_common = mouss.intersection(sylv1)
    print("mouss vs sylv1 common:", mouss_sylv1_common)

    mouss_unique = mouss.difference(sylv1)
    print("mouss unique:", mouss_unique)

    sylv1_unique = sylv1.difference(mouss)
    print("sylv1 unique:", sylv1_unique)


if __name__ == "__main__":
    ft_achievement_tracker()
