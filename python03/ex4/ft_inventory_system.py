inventory = {
    "potion": 5,
    "armor": 3,
    "shield": 2,
    "sword": 1,
    "helmet": 1,
}


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")

    total_items = 0
    for quantity in inventory.values():
        total_items += quantity
    unique_types = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")
    print("\n=== Current Inventory ===")

    tot = total_items

    for item, quantity in inventory.items():
        percentage = (quantity / tot) * 100

        unit_label = "unit" if quantity == 1 else "units"
        print(f"{item}: {quantity} {unit_label} ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_item = None
    least_item = None

    for item, quantity in inventory.items():
        if most_item is None or quantity > inventory[most_item]:
            most_item = item
        if least_item is None or quantity < inventory[least_item]:
            least_item = item

    print(f"Most abundant: {most_item} ({inventory[most_item]} units)")
    print(f"Least abundant: {least_item} ({inventory[least_item]} units)")

    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}

    for item, quantity in inventory.items():
        if quantity >= 5:
            moderate[item] = quantity
        else:
            scarce[item] = quantity

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    for item, quantity in inventory.items():
        if quantity == 1:
            print("Restock needed:", item)

    print("\n=== Dictionary Properties Demo ===")
    keys_ordered = ["sword", "potion", "shield", "armor", "helmet"]
    values_ordered = [inventory[key] for key in keys_ordered]

    print("Dictionary keys:", keys_ordered)
    print("Dictionary values:", values_ordered)
    print("\nSample lookup - 'sword' in inventory:", "sword" in inventory)


def main() -> None:
    ft_inventory_system()


if __name__ == "__main__":
    main()
