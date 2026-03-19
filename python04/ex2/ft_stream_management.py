import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id = input("Input Stream active. Enter archivist ID: ")
    Status = input("Input Stream active. Enter status report: ")

    print(f'[STANDARD] Archive status from {id} : {Status}')
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys. stderr
        )
    print("[STANDARD] Data transmission complete\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
