'''
flowerpot
author; Kaki Weiksner
Date:11/27/23
despriction;This code allows a player to play rock paper sissors against a computer or against another player. This code counts the score and allows to play multiple rounds.
bugs;none
challenges;You can play against the computer or against a friend, there is a score counter and it tells who is winning at the end of each round and at the end of the game. I used str.upper and str.lower to eliminate as much error as possible. I used while True loops to make sure that if the user did not imput the right answer to the question that it would ask them again. I also used player names. Lastly, if both player pick s then the code ends. 
'''

import random                                                                                        #introducing random library into the code 
import sys                                                                                           #intoducing sys library into the code

print("Let's Play Rock paper Sissors")                                                               #displays lets play rock paper sissors
player1_score = 0                                                                                    #player score 1 is 0
player2_score = 0                                                                                    #player score 2 is 0
rps_computer = ["R","P", "S"]                                                                        #a list that has r,p or s

while True:                                                                                          #an infinate loop until it is manually broken
    while True:                                                                                      #an infinate loop until it is manually broken
        play = str.lower(input("Do you want to play against the computer or against a friend: "))    #asks user if they want to play against a computor or against another person
        print()                                                                                      #displays a line with no writing
        
        if play not in ["friend", "computer"]:                                                       #if friend or computer is not in the question do you want to play against the computer or against a friend                                                     
            print("Remember to choose friend or computer")                                           #displays remembre to choose friend or computer
        else:
            player1 = input("player 1, what is your name?")                                          #asks player 1 for there name

            while True:                                                                              #an infinate loop until manually brocken
                player1_pick = str.upper(input(f"{player1}, do you want to pick r,p or s"))          #calls player 1 by there name and asks them to pick r,p or s
                print()                                                                              #displays a line with no writing

                if player1_pick not in rps_computer:                                                 #if the player pick is not in the rps_computer list
                    print("Invalid")                                                                 #displays invalid
                else:
                    break                                                                            #manually breaks loop
                
            if play == "computer":                                                                   #if the user wants to play against the computer
                player2_pick = random.choice(rps_computer)                                           #player 2 is a random computer choice
                player2 = "computer"                                                                 #the name for player 2 is computer 
                break                                                                                #manually breaks loop
            elif play == "friend":                                                                   #if the user wants to play against a friend
                player2 = input("Player 2, what is your name?")                                      #asks player 2 for their name
                print()                                                                              #displays a line with no writing
                while True:                                                                          #an infinate loop until it is manually broken
                    player2_pick = str.upper(input(f"{player2}, do you want to pick r,p or s"))
                    print()                                                                          #displays a line with no writing

                    if player2_pick not in rps_computer:                                             #if player 2's pick is not in the rps computer list 
                        print("Invalid")                                                             #displays invalid
                    else:
                        break                                                                        #manually breaks loop
                break                                                                                #manually breaks loop

    if player1_pick == "R" and player2_pick == "R" or player1_pick == "P" and player2_pick == "P":   #if player one and player 2 pick the same weapon except for s and s
        print("It is a draw, you guys picked the same thing.")                                       #displays its a draw, you guys picked the same thing
    elif player1_pick == "S" and player2_pick == "S":                                                #if both players pick s
        print("You broke the code")                                                                  #displays you broke the code
        sys.exit()                                                                                   #Exits all of the code
    elif player1_pick == "R" and player2_pick == "S" or player1_pick == "S" and player2_pick == "P" or player1_pick == "P" and player2_pick == "R":#if player 1 plays something that beats player 2
        print(f"{player1} wins")                                                                     #displays player 1 wins
        player1_score += 1                                                                           #player 1 score adds one
    elif player2_pick == "R" and player1_pick == "S" or player2_pick == "S" and player1_pick == "P" or player2_pick == "P" and player1_pick == "R":#if player 1 plays something that beats player 2
        print(f"{player2} wins")                                                                     #displays player 2 wins
        player2_score += 1                                                                           #player 2 score adds one
    else:
        print("Remember both players should either do r,p, or s")                                    #if either user does not put r, p or s then it displays Remember both players should either do r,p, or s

    while True:                                                                                      #an infinate loop until it is manually broken
        play_again = str.lower(input("Do you want to play agian\n"))                                   #asks if they want to play again                                                                                 #displays a line with no writing

        if play_again == "yes":
            print(f"the {player2} score is {player2_score}")                                         #displays the player 1 score
            print(f"the {player1} score is {player1_score}")                                         #displays the plater 2 score
            break
        elif play_again == "no":
            print(f"the Final{player2} score is {player2_score}")                                    #displays the player 1 score
            print(f"the Final{player1} score is {player1_score}")                                    #displays the plater 2 score
            if player1_score > player2_score:
                print(f"Congradulations, {player1} wins")                                            #if the player 1 score is grater than the player 2 score than in dipsplays, congradulations player 1 wins
            elif player1_score < player2_score:
                print(f"Congradulations, {player2} wins")                                            #if the player 2 beats the player 1, the computer displays congradualtion, player one wins
            elif player1_score == player2_score:
                print("It was a tie")                                                                #if the player 2's score and player 1's scores are tied, then it displayes it was a tie. 
                print("Thanks for playing")                                                          #displays thanks for playing
            sys.exit()                                                                               #Exits all of the code
        else:
            print("Remeber to pick yes or no")                                                       #displays remember to pick yes or no 

    
    
