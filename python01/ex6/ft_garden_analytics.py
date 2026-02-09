# Base plant class
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def show_prize(self):
        print(f"Prize points: {self.prize_points}")


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(
                    f"- {plant.name}: {plant.height}cm,"
                    f"{plant.color} flowers (blooming), "
                    f"Prize points: {plant.prize_points}"
                    )
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm,"
                      f"{plant.color} flowers (blooming)"
                      )
            else:
                print(f"- {plant.name}: {plant.height}cm")


class GardenManager:
    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        print("Garden network created")

    @staticmethod
    def validate_height(height):
        return height >= 0

    class GardenStats:
        @staticmethod
        def count_plants(plants):
            return len(plants)

        @staticmethod
        def total_growth(plants):
            return len(plants)

        @staticmethod
        def plant_types(plants):
            reg = 0
            flow = 0
            prz = 0

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prz += 1
                elif isinstance(plant, FloweringPlant):
                    flow += 1
                else:
                    reg += 1

            return reg, flow, prz


def main():
    print("=== Garden Analytics ===")

    manager = GardenManager()
    alice_garden = Garden("Alice")

    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 60, "yellow", 10)

    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()
    alice_garden.report()

    print(f"Plants in garden: "
          f"{GardenManager.GardenStats.count_plants(alice_garden.plants)}")
    print(f"Total growth: "
          f"{GardenManager.GardenStats.total_growth(alice_garden.plants)}cm")
    reg, flow, prz = GardenManager.GardenStats.plant_types(alice_garden.plants)
    print(f"Plant types: {reg} regular, {flow} flowering, {prz} prize flowers")
    manager.add_garden(alice_garden)
    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
