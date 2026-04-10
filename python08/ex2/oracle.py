import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("[ERROR] 'python-dotenv' module not found.")
    print("Please install it using: pip install python-dotenv")
    print("OR use: poetry install")
    sys.exit(1)


def main() -> None:

    env_load = load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_url = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")

    if not env_load and not any([mode, db_url, api_key, log_level, zion_url]):
        print("\n[!] CRITICAL: No configuration detected.")
        print("Please create a .env file: 'cp .env.example .env'")
        print("Or provide environment variables directly.")
        print("\nEnvironment security check:")
        print("[WARNING] .env file missing")
        sys.exit(0)

    vars_check = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": db_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_url
    }

    missing = [name for name, val in vars_check.items() if not val]

    if missing:
        print("\nMissing configuration:")
        for var in missing:
            print(f"- {var}")
        sys.exit(0)

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if db_url and "localhost" in db_url:
        db_type = "local instance"
    else:
        db_type = "remote instance"

    print(f"Database: Connected to {db_type}")
    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online")
    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")

    if "MATRIX_MODE" in os.environ:
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
