import json
from purchase import purchase_item

def shopkeeper_interaction():
    # Load shop inventory
    with open('shop_inventory.txt', 'r') as file:
        shop_inventory = json.load(file)

    print()
    print("Shopkeeper: Hello, adventurer!")
    print()

    if input("Shopkeeper: Would you like to see my wares? (yes/no) ").strip().lower() == "yes":
        print()
        print("Shopkeeper: Excellent, here they are!")
        print()
        for key, item in shop_inventory.items():
            print(f"{key} costs {item} gp")
        print()
        print("Shopkeeper: What takes your fancy adventurer?")
        print()
        requested_item = input("Type the name of the item you wish to purchase: ").strip()

        if requested_item in shop_inventory:
            try:
                purchase_item(requested_item)
                print(f"Shopkeeper: You have successfully purchased {requested_item}!")
            except ValueError as e:  # Handling errors like insufficient funds
                print(f"Shopkeeper: {e}")
            except Exception as e:  # General exception to catch unexpected errors
                print(f"Shopkeeper: An error occurred: {e}")
        else:
            print("Shopkeeper: Sorry, we don't have that item.")
    else:
        print()
        print("Shopkeeper: Begone then!")

if __name__ == "__main__":
    shopkeeper_interaction()