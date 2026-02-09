class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.td = trunk_diameter

    def produce_shade(self):
        shade_area = self.td * 1.56
        print(f"{self.name} provides {int(shade_area)} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.hs = harvest_season
        self.nv = nutritional_value


def main():
    print("=== Garden Plant Types ===")

    # Flowers
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    tulip.bloom()
    print(f"{rose.name} {rose.height}cm, {rose.age} days, {rose.color} color")
    rose.bloom()

    # Trees
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)

    pine.produce_shade()
    print(f"{oak.name} {oak.height}cm, {oak.age} days, {oak.td}cm diameter")
    oak.produce_shade()

    # Vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "spring", "vitamin A")

    carrot.hs = "early spring"
    print(f"{tomato.name} {tomato.height}cm,{tomato.age}d,{tomato.hs} harvest")
    print(f"{tomato.name} is rich in {tomato.nv}")


if __name__ == "__main__":
    main()
