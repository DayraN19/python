import sys
import os
import importlib.util
import importlib
from typing import Dict

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def check_dependencies(packages: list) -> Dict[str, str]:
    versions = {}
    print("Checking dependencies:")
    for pkg in packages:
        spec = importlib.util.find_spec(pkg)
        if spec is None:
            print(f"[ERROR] {pkg} is missing!")
            print("To install: pip install -r requirements.txt OR"
                  "poetry install")
            sys.exit(1)

        module = importlib.import_module(pkg)
        version = getattr(module, "__version__", "unknown")
        versions[pkg] = version
        print(f"[OK] {pkg} ({version}) - Ready")
    return versions


def detect_manager() -> str:
    if ("poetry" in sys.executable.lower()
            or os.path.exists("../pyproject.toml")):
        return "Poetry (Advanced Dependency Management)"
    return "Pip/Venv (Standard Requirements)"


def run_analysis() -> None:
    try:
        print("\nAnalyzing Matrix data...")
        data = np.random.randn(1000)
        df = pd.DataFrame(data, columns=["Matrix Data"])
        print(f"Processing {len(df)} data points...")

        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.hist(df["Matrix Data"], bins=30, color='blue', alpha=0.7)
        plt.title("Matrix Data Distribution")
        plt.grid(True, alpha=0.3)

        plt.savefig("matrix_analysis.png")
        plt.close()
        print("Analysis complete! Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"[ERROR] An analysis error occurred: {e}")
        sys.exit(1)


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    packages = ["pandas", "numpy", "matplotlib", "requests"]
    check_dependencies(packages)

    print(f"\nMODE: Running with {detect_manager()}")

    run_analysis()


if __name__ == "__main__":
    main()
