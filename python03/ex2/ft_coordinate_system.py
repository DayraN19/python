import math


def ft_coordinate_system(
        x: int, y: int, z: int
) -> tuple[tuple[int, int, int], float]:
    position = (x, y, z)
    distance = math.sqrt(x**2 + y**2 + z**2)
    print(f"Position created: {position}")
    print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")
    return position, distance


def parse_coordinates(coord_str: str) -> tuple[int, int, int] | None:
    try:
        x_str, y_str, z_str = coord_str.split(",")

        print(f'Parsing coordinates: "{coord_str}"')

        x = int(x_str)
        y = int(y_str)
        z = int(z_str)

        position = (x, y, z)
        print(f"Parsed position: {position}")

        distance = math.sqrt(x**2 + y**2 + z**2)
        print(f"Distance between (0, 0, 0) and {position}: {distance:.1f}")
        return position

    except ValueError as e:
        print(f'Parsing invalid coordinates: "{coord_str}"')
        print(f"Error parsing coordinates: {e}")
        print(
            "Error details - Type: ValueError, "
            f"Args: {e.args}"
        )
        return None


def main() -> None:
    print("=== Game Coordinate System ===")

    pos1, dist1 = ft_coordinate_system(10, 20, 5)

    coord_str = "3,4,0"
    pos2 = parse_coordinates(coord_str)

    invalid_str = "abc,def,ghi"
    parse_coordinates(invalid_str)

    if pos2:
        x, y, z = pos2
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
