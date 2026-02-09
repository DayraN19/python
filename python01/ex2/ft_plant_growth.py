class Plant:
    """Plant class with growth and aging behaviors"""
    def __init__(self, name, height, age, growth_rate=2):
        self.name = name
        self.height = height
        self.days_old = age
        self.growth_rate = growth_rate

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.days_old += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm tall, {self.days_old} days old"

    def display(self):
        print(self.get_info())


def simulate_week(plants):
    print("=== Day 1 ===")
    for day in range(1, 8):
        if day == 1:
            for plant in plants:
                plant.display()
        else:
            for plant in plants:
                plant.grow()
                plant.age()
            if day == 7:
                print(f"=== Day {day} ===")
                for plant in plants:
                    plant.display()

    for plant in plants:
        total_growth = plant.growth_rate * 6
        print(f"Grow this week: +{total_growth}cm")


def main():
    plant1 = Plant("Rose", 25, 30, growth_rate=1)

    plants = [plant1]

    simulate_week(plants)


if __name__ == "__main__":
    main()
