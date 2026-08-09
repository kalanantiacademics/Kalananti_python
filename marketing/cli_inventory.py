import time
import os

# --- Data Storage (List of Dictionaries) ---
inventory = [
    {"name": "Laptop", "price": 15000000, "stock": 5},
    {"name": "Mouse", "price": 150000, "stock": 20},
    {"name": "Keyboard", "price": 300000, "stock": 15}
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    clear_screen()
    print("\033[1;36m") # Cyan color
    print(r"""
  _  __     _                          _   _ 
 | |/ /    | |                        | | (_)
 | ' / __ _| | __ _ _ __   __ _ _ __ | |_ _ 
 |  < / _` | |/ _` | '_ \ / _` | '_ \| __| |
 | . \ (_| | | (_| | | | | (_| | | | | |_| |
 |_|\_\__,_|_|\__,_|_| |_|\__,_|_| |_|\__|_|
                                            
    INVENTORY SYSTEM (CLI) - LEVEL 2
    """)
    print("\033[0m") # Reset color
    print("="*50)
    print()

def view_items():
    show_header()
    print(f"{'No':<4} {'Item Name':<20} {'Price (IDR)':<15} {'Stock':<10}")
    print("-" * 50)
    for index, item in enumerate(inventory):
        print(f"{index + 1:<4} {item['name']:<20} {item['price']:<15,} {item['stock']:<10}")
    print("-" * 50)
    input("\nPress Enter to return to menu...")

def add_item():
    show_header()
    print("--- Add New Item ---")
    name = input("Enter item name: ")
    try:
        price = int(input("Enter price: "))
        stock = int(input("Enter stock: "))
        inventory.append({"name": name, "price": price, "stock": stock})
        print(f"\nScanning item '{name}'...")
        time.sleep(1) # Simulate processing
        print("Success! Item added.")
    except ValueError:
        print("\nError: Price and Stock must be numbers!")
    
    input("\nPress Enter to return to menu...")

def search_item():
    show_header()
    print("--- Search Item ---")
    query = input("Enter item name to search: ").lower()
    found = False
    print(f"\n{'No':<4} {'Item Name':<20} {'Price (IDR)':<15} {'Stock':<10}")
    print("-" * 50)
    for index, item in enumerate(inventory):
        if query in item['name'].lower():
            print(f"{index + 1:<4} {item['name']:<20} {item['price']:<15,} {item['stock']:<10}")
            found = True
    print("-" * 50)
    if not found:
        print("No items found.")
    input("\nPress Enter to return to menu...")

def main():
    while True:
        show_header()
        print("1. View Inventory")
        print("2. Add New Item")
        print("3. Search Item")
        print("4. Exit")
        print("-" * 40)
        
        choice = input("Select Menu (1-4): ")
        
        if choice == '1':
            view_items()
        elif choice == '2':
            add_item()
        elif choice == '3':
            search_item()
        elif choice == '4':
            print("\nThank you for using Kalananti Inventory System!")
            break
        else:
            print("\nInvalid choice, please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
