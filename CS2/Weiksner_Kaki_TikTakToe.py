'''
Flower Box
Name: Kaki Weiksner 
    Description: Allows 2 People to play Tik Tak Toe 
    Bugs: There are no bugs that I have found 
    Features: None
    Logs: 1.0 intial release 11/22 
    Sources: Mr Campell
'''

import sys          # importats file sys 

def print_board(box):
    """
    Args: 
        box(array): An array of the box 
    Prints:
        prints the box  
    """
    # i is row, j is column
    for i in range(len(box)):                   #iterates through the row              
        print()
        for j in range(len(box[i])):            #iterates through the column
            print(box[i][j], end='')
    print()

def turn(box, player_pick,player_letter): 
    """
    Args: 
        box(array): an array of the current box
        player_pick(int): The number represented spot that they want to go  
        player_letter(str):either x or o 
    Retuns:
        bolean: False 
            if they entered something wrong 
    Prints: 
        the new board box
    """
    
    #puts the players turn into the box
    if player_pick == 1:
        #sees if the the box is already taken  
        if box[0][0] == 1:
            box[0][0] = player_letter
        else: 
            return False
    elif player_pick == 2: 
        if box[0][1] == 2:
            box[0][1] = player_letter
        else: 
            return False
    elif player_pick == 3: 
        if box[0][2] == 3:
            box[0][2] = player_letter
        else: 
            return False
    elif player_pick == 4:
        if box[1][0] == 4:
            box[1][0] = player_letter
        else: 
            return False
    elif player_pick == 5:
        if box[1][1] == 5:
            box[1][1] = player_letter
        else: 
            return False 
    elif player_pick == 6:
        if box[1][2] == 6:
            box[1][2] = player_letter
        else: 
            return False 
    elif player_pick == 7: 
        if box[2][0] == 7:
            box[2][0] = player_letter
        else: 
            return False
    elif player_pick == 8: 
        if box[2][1] == 8:
            box[2][1] = player_letter
        else: 
            return False
    elif player_pick == 9: 
        if box[2][2] == 9:
            box[2][2] = player_letter
        else: 
            return False
    else: 
        return False

    print_board(box)

def check_win(box, player_letter):
    """
    Args: 
        box(array): an array of the current box
        player_letter(str):either x or o 
    Retuns:
        bolean: True 
            if someone one
        bolean: False
            if no one has one
    Print 
        the new board box
    """
    #sees if one of the player that just went won by seeing if there letter is 3 in a row
    if box[0][0] == player_letter and box[0][1] == player_letter and box[0][2] == player_letter or box[1][0] == player_letter and box[1][1] == player_letter and box[1][2] == player_letter or box[2][0] == player_letter and box[2][1] == player_letter and box[2][2] == player_letter: 
        return True 
    elif box[0][0] == player_letter and box[1][0] == player_letter and box[2][0] == player_letter or box[0][1] == player_letter and box[1][1] == player_letter and box[2][1] == player_letter or box[0][2] == player_letter and box[1][2] == player_letter and box[2][2] == player_letter:
        return True  
    elif box [0][0] == player_letter and box[1][1] == player_letter and box[2][2] == player_letter or box[0][2] == player_letter and box[1][1] == player_letter and box[2][0]== player_letter:
        return True 
    else:  
        return False 
        
def main (): 
    while True: 
        print("Welcome to Tik Tac Toe")
        #orginal array for the box
        box = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

        print_board(box)            #call function print_board with one parameter 

        while True: 
            #asks player 1 if they are x or o 
            player1_letter = str.lower(input("Player 1 are you x or o: "))
            if player1_letter == "x":
                player2_letter = "o"
                break
            elif player1_letter == "o": 
                player2_letter = "x"
                break
            else: 
                print("Enter x or o")
        count=0                                         #sets count to zero which is how many moves
        
        while count <= 9:                               #infinate loop for the game while count is less than nine
            while True:                                 #infinate loop for if their play is valid 
                while True:                             #infinate loop for if their pick is an integer
                    player1_pick = input("Player one pick which spot you would like to go: ")
                    # sees if player 1 pick is an integer 
                    try: 
                        player1_pick = int(player1_pick)
                        if player1_pick >=1 and player1_pick <=9:
                            break
                    except ValueError:
                        print("You did not enter the correct information")
                    
                valid_play = turn(box, player1_pick, player1_letter)            #calls the function turn with 3 parameters
                if valid_play == False: 
                    print("You did not enter a valid turn")
                else:
                    break

                
            #checks if player one won 
            if check_win(box, player1_letter): 
                print("Player 1 Wins!")
                break
            count += 1              #adds one to the counter 

            #if the counter is 9, then it is a tie 
            if count == 9:
                print("It is a tie")
                break
            while True:             #an infinate loop for player 2s turn 
                while True:          #an infinate loop to make sure player 2s pick is an integer
                    player2_pick = input("Player two pick which spot you would like to go: ")
                    # sees if player 1 pick is an integer 
                    try: 
                        player2_pick = int(player2_pick)
                        if player2_pick >=1 and player2_pick <=9:
                            break
                    except ValueError:
                        print("You did not enter the correct information")
                # makes sure the turn is valid 
                valid_play = turn(box, player2_pick, player2_letter)
                if valid_play == False: 
                    print("You did not enter a valid turn")
                else:
                    break
            
            #checks if player one won 
            if check_win(box, player2_letter) == True:
                print("Player 2 Wins") 
                break
            count += 1 #adds one to count
        
        #asks user if they want to play again
        while True:
            play_again = str.lower(input("Would you like to play again"))
            if play_again == "no":
                exit()
            elif play_again == "yes":
                break  
            else: 
                print("You did not enter yes or no")

main()
