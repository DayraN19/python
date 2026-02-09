import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")

    # No scores provided
    if len(sys.argv) < 2:
        print("No scores provided.")
        return

    scores = []

    # Parse arguments
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid score ignored: {arg}")

    # If all inputs were invalid
    if len(scores) == 0:
        print("No valid scores to analyze.")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


def main():
    ft_score_analytics()


if __name__ == "__main__":
    main()
