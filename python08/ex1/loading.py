import sys
import importlib.util
import os

packages = ["pandas", "numpy", "matplotlib", "requests"]

print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")

for pkg in packages:
    spec = importlib.util.find_spec(pkg)
    
    if spec is None:
        print(f"[ERROR] {pkg} is missing!")
        print("To install: pip install -r requirements.txt")
        sys.exit(1)
    else:
        module = importlib.import_module(pkg)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {pkg} ({version}) - Ready")

if "poetry" in sys.executable.lower():
    print("\nMODE: Running with Poetry environment")
else:
    print("\nMODE: Running with Pip/Venv environment")

print("Analyzing Matrix data...")
# Utilise numpy pour générer 1000 points (ex: np.random.randn(1000))
# Utilise pandas pour les mettre dans un DataFrame
# Affiche "Processing 1000 data points..."

# 5. GÉNÉRATION DU GRAPHIQUE
print("Generating visualization...")
# Importe matplotlib.pyplot as plt (fais-le ici ou en haut)
# Crée un graphique simple (plt.plot ou plt.hist)
# SAUVEGARDE : plt.savefig("matrix_analysis.png")

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")