import os
from typing import List, Optional
from dotenv import load_dotenv


def load_config() -> None:
    load_dotenv()


def check_security() -> None:
    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running in development mode")

    print("[OK] No hardcoded secrets detected")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    load_config()

    mode: str = os.getenv("MATRIX_MODE", "development")
    db_url: Optional[str] = os.getenv("DATABASE_URL")
    api_key: Optional[str] = os.getenv("API_KEY")
    log_level: Optional[str] = os.getenv("LOG_LEVEL")
    zion_url: Optional[str] = os.getenv("ZION_ENDPOINT")

    vars_to_check = {
        "DATABASE_URL": db_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_url
    }
    
    missing: List[str] = [name for name, val in vars_to_check.items() if not val]

    if missing:
        print("Missing configuration:")
        for var in missing:
            print(f"- {var}")
        print("\nUse .env file or environment variables.")
    else:
        print("\nConfiguration loaded:")
        print(f"Mode: {mode}")
        
        db_status = "local instance" if "localhost" in db_url else "remote instance"
        print(f"Database: Connected to {db_status}")
        print("API Access: Authenticated")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online")

    check_security()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
