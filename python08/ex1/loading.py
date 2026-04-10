import sys
import importlib.util
from typing import Dict

REQUIRED_PACKAGES: list[str] = ["pandas", "numpy", "matplotlib", "requests"]


def check_dependencies(packages: list[str]) -> Dict[str, str]:
    versions: Dict[str, str] = {}
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    missing_any = False

    for pkg in packages:
        try:
            spec = importlib.util.find_spec(pkg)
            if spec is None:
                print(f"[ERROR] {pkg} is missing!")
                missing_any = True
                continue

            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            versions[pkg] = version

            labels = {
                "pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "matplotlib": "Visualization ready",
                "requests": "Network access ready",
            }
            print(f"[OK] {pkg} ({version}) - {labels.get(pkg, 'Ready')}")

        except Exception as e:
            print(f"[ERROR] Could not load {pkg}: {e}")
            missing_any = True

    if missing_any:
        print("\nMissing dependencies detected.")
        print("Install with:pip install -r requirements.txt OR poetry install")
        sys.exit(1)

    return versions


def analyze_data() -> None:
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")

        data = np.random.randn(1000)
        df = pd.DataFrame(data, columns=["values"])
        print(f"Processing {len(df)} data points...")

        print("Generating visualization...")
        plt.figure(figsize=(8, 5))
        plt.hist(df["values"], bins=30, color='green', alpha=0.7)
        plt.title("Matrix Data Distribution")
        plt.savefig("matrix_analysis.png")
        plt.close()

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    except ImportError as e:
        print(f"[ERROR] Missing library during execution: {e}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")


def main() -> None:
    check_dependencies(REQUIRED_PACKAGES)
    analyze_data()


if __name__ == "__main__":
    main()
