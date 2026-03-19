import alchemy.grimoire
print("\n=== Circular Curse Breaking ===\n")
print("Testing ingredient validation:")
print(f'validate_ingredients("fire air"):'
      f'{alchemy.grimoire.validate_ingredients("fire air")}')
print(f'validate_ingredients("dragon scales"):'
      f'{alchemy.grimoire.validate_ingredients("dragon scales")}\n')

print("Testing spell recording with validation:")
print(f'record_spell("Fireball", "fire air"):'
      f'{alchemy.grimoire.record_spell("Fireball", "fire air")}')
print(f'record_spell("Dark magic", "shadow"):'
      f'{alchemy.grimoire.record_spell("Dark magic", "shadow")}\n')

print("Testing late import technique:")
print(f'record_spell("Lightning", "air"):'
      f'{alchemy.grimoire.record_spell("Lightning", "air")}')

print("Circular dependency curse avoided")
