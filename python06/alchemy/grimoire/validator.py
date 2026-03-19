def validate_ingredients(ingredients: str) -> str:
    valid_elements = {"fire", "water", "earth", "air"}
    items = [item.strip() for item in ingredients.split()]

    if any(item in valid_elements for item in items):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
