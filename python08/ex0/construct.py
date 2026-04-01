import sys
import os
import site


def construct() -> bool:
    if sys.prefix == sys.base_prefix:
        return True
    else:
        return False


if construct() is True:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate     # On Windows\n")
    print("Then run this program again.")

if construct() is False:
    print("\n MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)} ")
    print(f"Environment path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print(f"Package installation path:\n {site.getsitepackages()[0]}")


def main() -> None:
    construct()


if __name__ == "__main__":
    main()
