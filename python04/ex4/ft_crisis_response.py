def crisis_handler(filename):
    try:
        # Détection du type d'accès
        if filename == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")

        # Tentative d'ouverture sécurisée
        with open(filename, "r") as f:
            content = f.read()

        # Succès
        print(f"SUCCESS: Archive recovered - ``{content.strip()}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled with failsafe protocols")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    # Crises simulées
    crisis_handler("lost_archive.txt")          # n'existe pas
    crisis_handler("classified_vault.txt")      # permissions interdites
    crisis_handler("standard_archive.txt")      # fichier normal

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
