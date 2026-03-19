class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!\n"


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        shade_area: float = self.trunk_diameter * 1.56
        return f"{self.name} provides {int(shade_area)} square meters of shade"


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main() -> None:
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")

    print(f"{rose.name} (Flower): {rose.height}cm,"
          f"{rose.age} days, {rose.color} color")
    print(rose.bloom())

    oak = Tree("Oak", 500, 1825, 50)

    print(
        f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
        f"{oak.trunk_diameter}cm diameter"
    )
    print(oak.produce_shade())

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print(
        f"\n{tomato.name} (Vegetable): {tomato.height}cm, "
        f"{tomato.age} days, {tomato.harvest_season} harvest"
    )
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")


if __name__ == "__main__":
    main()
