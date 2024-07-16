from shopkeeper import shopkeeper_interaction

def main_game_loop():
    while True:
        print()
        print("What would you like to do?")
        print()
        print("1. Visit the shopkeeper")
        print("2. Exit the game")
        print()
        choice = input("Enter the number of your choice: ").strip()

        if choice == "1":
            shopkeeper_interaction()
        
        else:
            print()

if __name__ == "__main__":
    main_game_loop()