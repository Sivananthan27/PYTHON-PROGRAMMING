Grocery = {
    "Cornflakes": {"quantity": 15, "price": 100},
    
    "Muesli": {"quantity": 14, "price": 150},
    "Oats": {"quantity": 10, "price": 80},
    "Wheat Flakes": {"quantity": 5, "price": 75},
    "Granola": {"quantity": 8, "price": 125}
}

# Display the initial dictionary
print("Initial Grocery Details:")
print(Grocery)
print()

# Get user input for stock update
print("What do you want to do?")
print("1. Add additional quantity of the cereals")
print("2. Update the price of the grocery")
print("3. Add a new item")
choice = int(input("Enter your choice: "))

# Perform stock update based on user's choice
if choice == 1:
    item_name = input("Enter the grocery item name: ")
    quantity_added = int(input("Enter the quantity of item to be added: "))

    if item_name in Grocery:
        Grocery[item_name]['quantity'] += quantity_added
    else:
        print("Item not found in the grocery list.")

elif choice == 2:
    item_name = input("Enter the grocery item name: ")
    new_price = float(input("Enter the updated price: "))

    if item_name in Grocery:
        Grocery[item_name]['price'] = new_price
    else:
        print("Item not found in the grocery list.")

elif choice == 3:
    item_name = input("Enter the new item name: ")
    quantity = int(input("Enter the quantity of the new item: "))
    price = float(input("Enter the price of the new item: "))

    Grocery[item_name] = {"quantity": quantity, "price": price}

else:
    print("Invalid choice!")

# Display the updated dictionary
print("\nItem details after updating:")
print(Grocery)

