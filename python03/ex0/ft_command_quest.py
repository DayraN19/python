import sys


def ft_command_quest(argv: list[str]) -> None:
    print("=== Command Quest ===")

    if len(argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
        print(f"Total arguments: {len(argv)}")
        return

    print(f"Program name: {argv[0]}")
    print(f"Arguments received: {len(argv) - 1}")

    index = 1
    for arg in argv[1:]:
        print(f"Argument {index}: {arg}")
        index += 1

    print(f"Total arguments: {len(argv)}")


def main() -> None:
    ft_command_quest(sys.argv)


if __name__ == "__main__":
    main()
