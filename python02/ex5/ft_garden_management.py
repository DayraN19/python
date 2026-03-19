class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str,
                           water_level: int, sun_h: int) -> None:

        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")

        if sun_h > 12:
            raise PlantError(f"Sunlight hours {sun_h} is too high (max 12)")
        if sun_h < 2:
            raise PlantError(f"Sunlight hours {sun_h} is too low (min 2)")

        print(f"{plant_name}: healthy (water: {water_level}, sun: {sun_h})")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print("Error adding plant:", e)

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print("Watering error:", e)

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
        manager.check_plant_health("lettuce", 15, 6)
    except GardenError as e:
        print("Error checking lettuce:", e)

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
