def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty.")
    if water_level < 1 or water_level > 10:
        raise ValueError("Water level must be between 1 and 10.")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("Sunlight hours must be between 2 and 12.")


def test_raise_errors():
    print("=== Garden Plants Health Checker ===")
    print("")
    print("Testing valid inputs...")
    try:
        check_plant_health("Tomato", 5, 6)
        print("Valid inputs passed without errors.")
    except ValueError as e:
        print("Unexpected error for valid inputs:", e)
    print("")
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print("Caught ValueError for empty plant name:", e)
    print("")
    print("Testing invalid water level...")
    try:
        check_plant_health("Tomato", 0, 6)
    except ValueError as e:
        print("Caught ValueError for invalid water level:", e)
    print("")
    print("Testing invalid sunlight hours...")
    try:
        check_plant_health("Lettuce", 5, 1)
    except ValueError as e:
        print("Caught ValueError for invalid sunlight hours:", e)
    print("")
    print("All raise error tests completed successfully!")


def main():
    test_raise_errors()


if __name__ == "__main__":
    main()
