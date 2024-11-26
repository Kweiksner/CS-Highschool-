import random

def print_board(box):
    for i in range(len(box)):
        print()
        for j in range(len(box[i])):
            print(box[i][j], end='')
    print()

        
##def turn(box, player_pick,player_letter): 
##    if player_pick == "1": 
##        box[0][0] = player_letter
##    elif player_pick == "2": 
##        box[1,0] = player_letter 
##    elif player_pick == "3": 
##        box[2,0] = player_letter 
##    elif player_pick == "4": 
##        box[0,1] = player_letter 
##    elif player_pick == "5": 
##        box[1,1] = player_letter 
##    elif player_pick == "6": 
##        box[2,1] = player_letter 
##    elif player_pick == "7": 
##        box[0,2] = player_letter 
##    elif player_pick == "8": 
##        box[1,3] = player_letter 
##    elif player_pick == "9": 
##        box[2,3] = player_letter 
##    else: 
##        return("false")
def main (): 

    print("Welcome to Tik Tac Toe")
    board_choices = ["1","2","3","4","5","6","7","8","9"]
    box = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]


    print_board(box)

##    number_players = input("How many players do you want to play with? ")
##
##    if number_players == 1: 
##        player_2 = "computer"
##    player1_letter = str.lower("Player 1 are you x or o")
##
##    if player1_letter == "x": 
##        player2_letter = "o"
##    elif player1_letter == "o": 
##        player2_letter = "x"

    print_board


main()
