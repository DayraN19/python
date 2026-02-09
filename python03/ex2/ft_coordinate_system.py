import math


def ft_coordinate_system(x, y, z):
    position = (x, y, z)
    distance = math.sqrt(x**2 + y**2 + z**2)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Distance from origin: {distance:.2f}")
    return (position, distance)


def parse_coordinates(coord_str):
    """Parse a coordinate string like '3,4,0' into a tuple, handle errors."""
    try:
        x_str, y_str, z_str = coord_str.split(",")
        x, y, z = int(x_str), int(y_str), int(z_str)
        position = (x, y, z)
        print(f"Parsed position: {position}")
        distance = math.sqrt(x**2 + y**2 + z**2)
        print(f"Distance from origin: {distance:.2f}")
        return position
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e)}, Args: {e.args}")
        return None


def main():
    print("=== Game Coordinate System ===")

    # Example 1: fixed position
    pos1, dist1 = ft_coordinate_system(10, 20, 5)

    # Example 2: parsing valid string
    coord_str = "3,4,0"
    pos2 = parse_coordinates(coord_str)

    # Example 3: parsing invalid string
    invalid_str = "abc,def,ghi"
    parse_coordinates(invalid_str)

    # Example 4: tuple unpacking demonstration
    if pos2:
        x, y, z = pos2
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
