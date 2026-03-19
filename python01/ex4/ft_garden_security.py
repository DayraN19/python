class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]\n")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


def main() -> None:
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)

    plant.set_height(-5)

    print(f"Current plant: {plant.name} ({plant.get_height()}cm,"
          f" {plant.get_age()} days)"
          )


if __name__ == "__main__":
    main()
