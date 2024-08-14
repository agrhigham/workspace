import random
import time

def get_player_name():
    player_name = input("Hello player, what is your name?: ")
    print()
    return player_name

def roll_dice():
    rolls = 0
    while True:
        roll_1 = random.randint(1,6)
        roll_2 = random.randint(1,6)
        rolls += 1
        print("Rolling...")
        print()
        time.sleep(1)
        print(f"Roll: {roll_1} & {roll_2}. Total: {roll_1 + roll_2}")
        print()
        time.sleep(1)
        if roll_1 + roll_2 == 6:
            break
    print(f"You took {rolls} rolls")    
    print()    
    return rolls
        
def main_game():
    print("Welcome to the game!")
    print()
    player_1_name = get_player_name()    
    print(f"Hello, {player_1_name}")
    print()
    player_2_name = get_player_name()
    print(f"Hello, {player_2_name}")
    print()
    time.sleep(2)
    print("Player 1, time to roll!")
    print()
    time.sleep(2)
    player_1_rolls = roll_dice()
    print("Player 2, time to roll!")
    print()
    time.sleep(2)
    player_2_rolls = roll_dice()
    time.sleep(2)
    print("And the winner is...")
    print()
    time.sleep(2)
    print("...")
    print()
    time.sleep(2)
    if player_1_rolls == player_2_rolls:
        print(f"Nobody! Its a draw! Both players rolled {player_1_rolls} times!")
    elif player_1_rolls < player_2_rolls:
        print(f"{player_1_name} wins! {player_1_name} rolled {player_1_rolls} times!")
    else:
        print(f"{player_2_name} wins! {player_2_name} rolled {player_2_rolls} times!")


if __name__ == "__main__":
    main_game()

