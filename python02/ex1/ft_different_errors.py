def garden_operations(arg: str) -> None:
    try:
        if arg == "value":
            int("abc")

        elif arg == "zero":
            10 / 0

        elif arg == "file":
            open("missing.txt", "r")

        elif arg == "key":
            plants = {"rose": 10}
            plants["missing_plant"]

    except ValueError as e:
        print(f"Caught ValueError: {e}")

    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    garden_operations("value")

    print("\nTesting ZeroDivisionError...")
    garden_operations("zero")

    print("\nTesting FileNotFoundError...")
    garden_operations("file")

    print("\nTesting KeyError...")
    garden_operations("key")

    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
