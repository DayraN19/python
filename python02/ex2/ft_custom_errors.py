class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def plant_problem() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_problem() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        plant_problem()
    except PlantError as e:
        print("Caught PlantError:", e)

    print("Testing WaterError...")
    try:
        water_problem()
    except WaterError as e:
        print("Caught WaterError:", e)

    print("Testing catching all garden errors...")
    try:
        plant_problem()
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        water_problem()
    except GardenError as e:
        print("Caught a garden error:", e)

    print("All custom error types work correctly!")


def main() -> None:
    test_custom_errors()


if __name__ == "__main__":
    main()
