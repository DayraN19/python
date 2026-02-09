def ft_command_quest(argv):
    if len(argv) < 2:
        print("Error: No Argument provided!")
        return

    print(f"Program name: {argv[0]}")
    print(f"Argument Provided: {len(argv)}")

    # Print each argument starting from index 1
    for i in range(1, len(argv)):
        print(f"Argument {i}: {argv[i]}")

    # Total arguments excluding program name
    print(f"Total Arguments: {len(argv)}")


def main():
    import sys
    ft_command_quest(sys.argv)


if __name__ == "__main__":
    main()
