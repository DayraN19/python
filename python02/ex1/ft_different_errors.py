def garden_operations():

    int("abc")

    10 / 0

    file = open("missing.txt", "r")
    file.close()

    plants = {"rose": 10}
    plants["missing_plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print("Caught ValueError:", e)

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)

    print("Testing KeyError...")
    try:
        plants = {"rose": 10}
        plants["missing_plant"]
    except KeyError as e:
        print("Caught KeyError:", e)

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, KeyError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
