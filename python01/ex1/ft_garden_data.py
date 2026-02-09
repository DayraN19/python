class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    print("=== Garden Plant Registry ===")

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    plants = [plant1, plant2, plant3]

    for i in range(len(plants)):
        plants[i].display()


if __name__ == "__main__":
    main()
