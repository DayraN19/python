class Plant:
    def __init__(self, name):
        self.name = name


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("Testing with error...")
    bad_plants = ["tomato", None, "lettuce"]
    water_plants(bad_plants)
    print("Cleanup always happens, even with errors!")


def main():
    test_watering_system()


if __name__ == "__main__":
    main()
