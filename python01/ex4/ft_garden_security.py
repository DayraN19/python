class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    # Setter sécurisé pour la hauteur
    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    # Setter sécurisé pour l'âge
    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    # Getters
    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


def main():
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)

    plant.set_height(-5)

    print(f"Current plant: {plant.name} ({plant.get_height()}cm,"
          f"{plant.get_age()} days)"
          )


if __name__ == "__main__":
    main()
