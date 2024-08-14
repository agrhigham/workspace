import random
from shopkeeper import shopkeeper_interaction

encounters_list = ["shop", "trap", "goblin", "death", "shop", "trap", "goblin", "death", "shop"]

def initialise_grid():
    # get a random selection of encounter triggers
    selected_encounters = random.sample(encounters_list, 9)
    random.shuffle(selected_encounters)
    # add each random encounter trigger to a tile from a 3x3 grid and return it
    grid = [[selected_encounters[i * 3 + j] for j in range(3)] for i in range(3)]
    return [[None]*3] + grid

def move(current_position):
    row = current_position[0] + 1
    col = int(input("Select your next tile (1-3): "))
    new_position = [row,col]
    return new_position

def main_game_loop():
    player_position = [0,0]
    grid = initialise_grid()

    while True:
        print("Welcome, to Adventure Quest!")
        print()
        player_position = move(player_position)
        print()
        
        
if __name__ == "__main__":
    main_game_loop()
        
        


