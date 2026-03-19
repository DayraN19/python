class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def show_prize(self) -> None:
        print(f"Prize points: {self.prize_points}")


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm,"
                      f"{plant.color} flowers (blooming),"
                      f"Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm,"
                      f"{plant.color} flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)


def create_garden_network(cls) -> None:
    print("Garden network created")


GardenManager.create_garden_network = classmethod(create_garden_network)


def validate_height(height: int) -> bool:
    return height >= 0


GardenManager.validate_height = staticmethod(validate_height)


class GardenManagerStats:
    def count_plants(plants: list[Plant]) -> int:
        return len(plants)

    count_plants = staticmethod(count_plants)

    def total_growth(plants: list[Plant]) -> int:
        return len(plants)

    total_growth = staticmethod(total_growth)

    def plant_types(plants: list[Plant]) -> tuple[int, int, int]:
        regular = 0
        flowering = 0
        prize = 0
        for plant in plants:
            if isinstance(plant, PrizeFlower):
                prize += 1
            elif isinstance(plant, FloweringPlant):
                flowering += 1
            else:
                regular += 1
        return regular, flowering, prize

    plant_types = staticmethod(plant_types)

    def garden_score(plants: list[Plant]) -> int:
        score = 0
        for plant in plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    garden_score = staticmethod(garden_score)


GardenManager.GardenStats = GardenManagerStats


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    oak = Plant("Oak Tree", 100, 10)
    rose = FloweringPlant("Rose", 25, 2, "red")
    sunflower = PrizeFlower("Sunflower", 50, 1, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()
    alice_garden.report()

    plants_added = GardenManager.GardenStats.count_plants(alice_garden.plants)
    total_growth = GardenManager.GardenStats.total_growth(alice_garden.plants)

    print(f"Plants added: {plants_added}, Total growth: {total_growth}cm")

    reg, flow, prz = GardenManager.GardenStats.plant_types(alice_garden.plants)
    print(f"Plant types: {reg} regular, {flow} flowering, {prz} prize flowers")

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    bob_tree = Plant("Pine", 90, 5)
    bob_garden.add_plant(bob_tree)

    alice_score = GardenManager.GardenStats.garden_score(alice_garden.plants)
    bob_score = GardenManager.GardenStats.garden_score(bob_garden.plants) + 2

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    main()
