def check_temperature(temp_str: str) -> int | None:
    try:
        print(f"Testing :{temp_str}")
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if temp < 0:
        print(f"Error: ({temp}) is too low! [REJECTED]\n")
    elif temp > 40:
        print(f"Error: ({temp}) is too high! [REJECTED]\n")
    elif temp == 25:
        print("Temperature is optimal. [OK]\n")
    return temp


def test_check_temperature() -> None:
    test_inputs = [25, 40, 0, -5, 'hot']
    for inp in test_inputs:
        result = check_temperature(inp)
        print(f"Returned: {result}")


def main() -> None:
    print("=== Temperature Checker ===")
    test_check_temperature()


if __name__ == "__main__":
    main()
    