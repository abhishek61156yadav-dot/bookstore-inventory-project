import json

# New book to add
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# ----------------------------
# Task 1 – Read the inventory
# ----------------------------
with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total books in inventory:", len(inventory))

# ----------------------------
# Task 2 – Update and save
# ----------------------------
inventory.append(new_book)

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

# ----------------------------
# Task 3 – Display inventory
# ----------------------------
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

print("\n--- Updated Book Inventory ---")
for book in updated_inventory:
    print(f"Title: {book['title']} |")
    print(f"Author: {book['author']} |")
    print(f"Price: ${book['price']}\n")
