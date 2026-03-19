def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open("vault_classified.txt", "r") as f:
        for line in f:
            print(f"[CLASSIFIED] {line.strip()}")

    print("\nSECURE PRESERVATION:")
    with open("vault_new_data.txt", "w") as f:
        f.write("New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
