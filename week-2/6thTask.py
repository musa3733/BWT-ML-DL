def update_inventory(inventory_dict, item, quantity):
    # Check if the item exists in the inventory
    if item in inventory_dict:
        # Update the quantity, ensuring it does not go below zero
        inventory_dict[item] = max(0, inventory_dict[item] + quantity)
    else:
        # If the item does not exist and the quantity to add is positive, add the item
        if quantity > 0:
            inventory_dict[item] = quantity
    return inventory_dict


def main():
    # Initialize an inventory dictionary with at least 5 items
    inventory = {
        "apples": 10,
        "bananas": 5,
        "oranges": 8,
        "grapes": 15,
        "pears": 7
    }

    # Prompt the user to update the inventory by adding or removing quantities of 3 items
    for _ in range(3):
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity to add/remove (use negative values for removal): "))
        inventory = update_inventory(inventory, item, quantity)

    # Display the updated inventory
    print("Updated Inventory:")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")


# Run the main function
if __name__ == "__main__":
    main()
