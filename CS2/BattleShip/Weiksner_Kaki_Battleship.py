'''
author; Kaki Weiksner
Date:2/11/25
despriction: Allows user to play battleship 
bugs: none
bonus:plays sound for hit or miss
tester: Nick Triplet
'''
import random
import sys
from playsound import playsound

def print_board(box):
    """
    Description:
        prints the box
    Args: 
        box(array): An array of the box 
    Prints:
        prints the box  
    """

    #i is row, j is column
    for i in range(len(box)):                   #iterates through the row   
        for j in range(len(box[i])):            #iterates through the column
            print(box[i][j], end='')
        print()

def place_ships(board,row_p, column_p):
    """"
    Description: Randomally places the Ships on the board
    Args:
       board(2d array): The Board to place the ships
       row_p(list): The list of all the row possiblities
       column_p(list):The list of all the column possiblities
    Returns:
        Viod
    Raises:
        None
    """
    n=5
    for i in range(n):
        while True:
            row = random.choice(row_p)
            new_row = int(row)
            column = random.choice(column_p)
            new_column=find_column(column)
            if board [new_row][new_column] == "🚢 ":                    # if the spot it is a ship continues 
                continue
            else:
                board[new_row][new_column] = "🚢 "                      #adds ship into the board
                break
    
def find_column(before_column):
    """"
    Description: Turns letter into a corresponding number so it can be put into the board
    Args:
       before_column(str or int): The letter or number of the column
    Returns:
        Column(int): The number of the corresponding number
    Raises:
        None
    """
    if before_column == "a" or before_column == 1:
        column = 1
    elif before_column == "b" or before_column == 2:
        column =2
    elif before_column == "c" or before_column == 3:
        column =3 
    elif before_column == "d" or before_column == 4:
        column =4 
    elif before_column == "e" or before_column == 5:
        column =5      
    else:
        print("You did not enter a letter a-e")
        return False
    return column

def check_hit(board_guesses,board,n_row, guess_column): 
    """"
    Description: Determins if the user hit a board
    Args:
       board(2d array): The Board to place the ships
       board_guesses(2d array): The board of the guess that the user has guessed
       n_row(str): The row the user of computer wants to go 
       column_p(str):The column where the user wants to go
    Returns:
        hit_miss(str): If the user hit or missed
        Flase(bolean): If the user already guessed that space 
    Raises:
        None
    """
    n_column = find_column(guess_column)
    row = int(n_row)
    column = int(n_column)
    if board[row][column] == "🚢 ":
        board_guesses[row][column] = "🔥 "
        board[row][column] = "🔥 "
        hit_miss = ("hit")
        return hit_miss
    elif board[row][column] == "🔥 " or board[row][column] == " x ":
        return False
    else:
        hit_miss = ("miss")
        board_guesses[row][column] = " x "
        board[row][column] = " x "
        return hit_miss

def main():
    user_board = [
        ["   "," a "," b "," c "," d "," e "],
        [" 1 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 2 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 3 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 4 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 5 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "]
        ]
    user_guesses = [
        ["   "," a "," b "," c "," d "," e "],
        [" 1 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 2 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 3 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 4 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 5 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "]
        ]
    computer_board = [
        ["   "," a "," b "," c "," d "," e "],
        [" 1 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 2 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 3 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 4 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 5 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "]
        ]
    computer_guesses = [
        ["   "," a "," b "," c "," d "," e "],
        [" 1 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 2 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 3 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 4 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "],
        [" 5 ","⬜ ","⬜ ","⬜ ","⬜ ","⬜ "]
        ]
    column_p = ["a", "b", "c", "d", "e"]
    row_p = ["1", "2", "3", "4", "5"]
    player_hit =0
    computer_hits = 0

    print("Welcome to battleship, you are playing against the computer, we have already placed ships for you, below is where your ships are palced")
    place_ships(user_board,row_p,column_p)
    print_board(user_board)
    place_ships(computer_board, row_p,column_p)

    play = "true"
    while play == "true":
        print("Here is your current guesses")
        print_board(user_guesses)
        
        user = 1
        hit = 1
        while user == 1:
            while hit == 1:
                column = 1
                row = 1
                hit = 1

                while column == 1:
                    #makes sure the user entered a letter a-e
                    user_column = str.lower(input("Which column would you like to guess their ship at (a-e): "))
                    if user_column in column_p: 
                        column = 2
                    else:
                        print("You did not enter a letter a-e")

                while row ==1:
                    #makes sure the user entered a number 1-5
                    user_row = input("Which row would you like to guess their ship at (1-5): ")
                    if user_row in row_p: 
                        row = 2
                    else:
                        print("You did not enter a number 1-5")
                hit_checker=check_hit(user_guesses,computer_board,user_row, user_column)

                #determines if the user has guessed that spot already
                if hit_checker == False:
                    print("You already guessed that spot")
                else:
                    hit = 2

            #plays sound if the user hit or missed a ship
            if hit_checker == "hit":
                player_hit += 1
                print("You Hit a ship")
                playsound("large-underwater-explosion-190270.mp3")
                user = 2
            elif hit_checker == "miss":
                print("You missed a ship")
                playsound("430a218f-aa11-429d-9c8d-aacff0ec3cd3.mp3")
                user =2 
            elif hit_checker == "You already guessed that":
                print("You already guessed that")
            else:
                print("You entered the wrong column or row")
            print_board(user_guesses)

            #determines if the player won
            if player_hit == 5:
                print("You win")
                sys.exit()
            
            comp = 0
            while  comp != 5:
                computer_column = random.choice(column_p)
                computer_rows = random.choice(row_p)
                computer_row = int(computer_rows)
                computer_col = int(find_column(computer_column))
                
                #determines if the computer has not guessed that already
                if computer_guesses[computer_row][computer_col] == "⬜ ":
                    hit_checker=check_hit(computer_guesses,computer_board,user_row, user_column)
                    print(f"The computer guessed: {computer_rows}{computer_column}")
                    comp = 5 

            #determines if the computer hit or missed a ship
            hit_checker=check_hit(computer_guesses,user_board,computer_row, computer_col)
            if hit_checker == "hit":
                computer_hits += 1
                print("The computer Hit a ship")
            elif hit_checker == "miss":
                print("The computer missed a ship")
            else:
                print("Unknown error")
                sys.exit()
            print("This is the computer gusses currently")
            print_board(user_board)
            
            #determines if the computer won
            if computer_hits == 5:
                print("The Computer Won")
                sys.exit()
   
main()