class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days_old = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days_old += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.days_old} days old"

    def display(self) -> None:
        print(self.get_info())


def simulate_week(plants: list[Plant]) -> None:
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
        total_growth = day - 1
        print(f"Growth this week: +{total_growth}cm")


def main() -> None:
    plant1 = Plant("Rose", 25, 30)

    plants: list[Plant] = [plant1]

    simulate_week(plants)


if __name__ == "__main__":
    main()
