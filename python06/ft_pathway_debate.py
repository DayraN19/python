import alchemy.transmutation
import alchemy.transmutation.basic
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
print("\n=== Pathway Debate Mastery ===\n")

print("Testing Absolute Imports (from basic.py):")
print(f"lead_to_gold():{alchemy.transmutation.basic.lead_to_gold()}")
print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}\n")

print("Testing Relative Imports (from advanced.py):")
print(f"philosophers_stone(): {philosophers_stone()}")
print(f"elixir_of_life(): {elixir_of_life()}\n")

print("Testing Package Access:")
print(f"alchemy.transmutation.lead_to_gold():"
      f"{alchemy.transmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone(): "
      f"{alchemy.transmutation.philosophers_stone()}\n")

print("Both pathways work! Absolute: clear, Relative: concise")
