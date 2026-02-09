# Custom exceptions
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("Not enough water in tank")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sun_h):
        if water_level < 1 or water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if sun_h < 2 or sun_h > 12:
            raise PlantError("Sunlight hours out of range")
        print(f"{plant_name}: healthy (water: {water_level}, sun: {sun_h})")


def test_garden_management():
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print("Error adding plant:", e)

    print("Watering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print("Watering error:", e)

    print("Checking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
        manager.check_plant_health("lettuce", 15, 6)
    except PlantError as e:
        print("Error checking lettuce:", e)

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")

    print("Garden management system test complete!")


def main():
    test_garden_management()


if __name__ == "__main__":
    main()
