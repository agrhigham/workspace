import json

def purchase_item(item):

    # Load shop inventory
    with open('shop_inventory.txt', 'r') as file:
        shop_inventory = json.load(file)

    # Load player gold
    with open('player_gold.txt', 'r') as file:
        player_gold = int(file.read())  # Convert to integer

    # Load player inventory
    with open('player_inventory.txt', 'r') as file:
        player_inventory = file.read().splitlines()

    if item in shop_inventory:
        purchase_value = int(shop_inventory[item])
    else:
        raise ValueError("Item not found in shop inventory!")

    if purchase_value <= player_gold:
        # Subtract the purchase value from player's gold
        player_gold -= purchase_value
        
        # Add the item to player's inventory
        player_inventory.append(item)
        
        # Save the updated gold amount
        with open('player_gold.txt', 'w') as file:
            file.write(str(player_gold))
        
        # Save the updated inventory
        with open('player_inventory.txt', 'w') as file:
            for inventory_item in player_inventory:
                file.write(f"{inventory_item}\n")
    else: 
        raise ValueError("Not enough gold!")