class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


def main():
    print("=== Plant Factory Output ===")

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant4 = Plant("Tulip", 30, 20)
    plant5 = Plant("Pivoine", 20, 15)
    plant6 = Plant("Orchid", 40, 50)

    plants = [plant1, plant2, plant3, plant4, plant5, plant6]

    for i in range(len(plants)):
        plants[i].display()
    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
