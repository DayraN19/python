def main() -> None:
    players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": ["first_kill", "level_10"],
            "region": "north",
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ["first_kill"],
            "region": "east",
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": ["level_10", "boss_slayer"],
            "region": "central",
        },
        {
            "name": "diana",
            "score": 2200,
            "achievements": ["first_kill", "boss_slayer"],
            "region": "north",
        },
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    scores_doubled = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if len(p["achievements"]) > 0]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players}

    score_categories = {
        "high": len([p for p in players if p["score"] > 2000]),
        "medium": len([p for p in players if 1500 <= p["score"] <= 2000]),
        "low": len([p for p in players if p["score"] < 1500])
    }

    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    active_regions = {p["region"] for p in players}

    unique_achievements = {
        ach for p in players for ach in p["achievements"]
    }

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(players)
    total_unique_ach = len(unique_achievements)
    avg_score = sum(p["score"] for p in players) / total_players

    leaderboard = sorted([(p["score"], p["name"],
                          len(p["achievements"])) for p in players],
                         reverse=True)
    top_score, top_name, top_ach = leaderboard[0]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_name} ({top_score} points,"
          f"{top_ach} achievements)")


if __name__ == "__main__":
    main()
