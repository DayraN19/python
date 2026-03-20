def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    filename: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    try:
        file = open(filename, "r")
        print("Connection established...\n")

        data: str = file.read()

        print("RECOVERED DATA:")
        print(data)

        file.close()
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first")


if __name__ == "__main__":
    main()
