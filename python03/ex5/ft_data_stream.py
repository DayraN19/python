from typing import Generator
import random
import time


PLAYERS = ["alice", "bob", "charlie", "diana", "eve", "frank"]
EVENT_TYPES = ["killed monster", "found treasure", "leveled up"]


def game_event_stream(n: int) -> Generator[dict, None, None]:
    for _ in range(n):
        yield {
            "player": random.choice(PLAYERS),
            "level": random.randint(1, 20),
            "event": random.choice(EVENT_TYPES),
        }


def fibonacci_stream() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream() -> Generator[int, None, None]:

    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    n_events = 1000
    print(f"Processing {n_events} game events...")

    events = game_event_stream(n_events)

    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    start = time.time()

    for j in range(n_events):
        event = next(events)
        print(
            f"Event {j+1}: Player {event['player']} "
            f"(level {event['level']}) {event['event']}"
        )

        total += 1
        if event["level"] >= 10:
            high_level += 1
        if event["event"] == "found treasure":
            treasure += 1
        if event["event"] == "leveled up":
            level_up += 1

    duration = time.time() - start

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration:.3f} seconds")

    print("=== Generator Demonstration ===")

    fib = fibonacci_stream()
    fib_list = [next(fib) for _ in range(10)]
    print("Fibonacci sequence (first 10):", end=" ")
    for k in range(len(fib_list)):
        print(fib_list[k], end="")
        if k != len(fib_list) - 1:
            print(",", end=" ")
    print()

    primes = prime_stream()
    prime_list = [next(primes) for _ in range(5)]
    print("Prime numbers (first 5):", end=" ")
    for k in range(len(prime_list)):
        print(prime_list[k], end="")
        if k != len(prime_list) - 1:
            print(",", end=" ")
    print()


if __name__ == "__main__":
    main()
