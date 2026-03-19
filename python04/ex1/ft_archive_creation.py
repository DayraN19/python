def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    print("Initializing new storage unit: new_discovery.txt")

    f = open("new_discovery.txt", "w")

    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")

    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    for entry in entries:
        f.write(entry + "\n")
        print(entry)

    f.close()

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
