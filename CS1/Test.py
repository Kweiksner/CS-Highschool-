
import random                                                                                                        #import random module   
import os                                                                                                            #import os module

print("cat")                                                                                                         #display message
print('Start')                                                                                                       #display message                                     
print('🪨📄✂️💧Welcome to Rock Paper Scissors and Water Game🪨📄✂️💧')                                           #display message
print("""                                                                                                               
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
""")                                                                                                                 #display message

p1_score = 0                                                                                                         #initialize player score
p2_score = 0                                                                                                         #initialize computer score               
score_limit = 5                                                                                                      #set score limit to 5 points               
valid_choices = ['rock', 'paper', 'scissors', 'water']                                                               #list of valid choices

print("Select Game Mode:")                                                                                           #display message     
print("1. Play against Computer (Enter 1)")                                                                          #display message       
print("2. Play against another Player (Enter 2)")                                                                    #display message

while True:                                                                                                          #forever loop
    mode = input("Enter your choice (1 or 2): ")                                                                     #prompt user for game mode choice   
    
    if mode in ['1', '2']:                                                                                           #if user input is valid                                                                                     
        break                                                                                                        #end forever loop                                                                      
    
print("first to", score_limit, "points wins the game!")                                                              #display message

p1_name = input('Player 1, enter your name: ')                                                                       #prompt player 1 for name                                                                                                    

if mode == '1': 
    print("You are playing a bot")                                                                                   #if user chose to play against computer
                                                                                                     
    p2_name = 'bot'                                                                                                  #set player 2 name to bot                      
else:                                                                                                                #if user chose to play against another player                       
    p2_name = input('Player 2, enter your name: ')                                                                   #prompt player 2 for name      

while True:                                                                                                          #forever loop                       
    p1_choice = input(f'{p1_name}, choose between rock, paper, scissors, or water: ').lower()                        #prompt player 1 for choice    
    
    if p1_choice not in valid_choices:                                                                               #if player 1 input is invalid 
        print('Invalid choice, please try again')                                                                    #display message
        continue
    if mode == '1':                                                                                                  #if user chose to play against computer                                     
        p2_choice = random.choice(valid_choices)                                                                     #set player 2 choice to a random valid choice          
    else:                                                                                                            #if user chose to play against another player                
        os.system('cls')                                                                                             #clear the console screen    
        while True:                                                                                                  #if user chose to play against another player
            p2_choice = input(f'{p2_name}, choose between rock, paper, scissors, or water: ').lower()                #prompt player 2 for choice

            if p2_choice in valid_choices:                                                                           #if player 2 input is valid 
                break                                                                                                #end forever loop 
        os.system('cls')                                                                                             #clear the console screen                      

    print(f'{p1_name} chose {p1_choice} {p2_name} chose {p2_choice}')                                                #display both players' choices      
    if p1_choice == p2_choice:                                                                                       #if both players chose the same option
        print('tie')                                                                                                 #display message
        continue                                                                                                     #continue forever loop                       
    elif p1_choice == 'rock':                                                                                        #if player 1 chose rock                 
        if p2_choice == 'scissors':                                                                                  #if player 2 chose scissors       
            print(f"{p1_name} wins")                                                                                 #display message                          
            p1_score += 1                                                                                            #increment player 1 score                     
        elif p2_choice == 'paper':                                                                                   #if player 2 chose paper                 
            print(f"{p2_name}wins")                                                                                  #display message               
            p2_score += 1                                                                                            #increment player 2 score                 
        elif p2_choice == 'water':                                                                                   #if player 2 chose water             
            print(f"{p1_name} wins")                                                                                 #display message                
            p1_score += 1                                                                                            #increment player 1 score
    elif p1_choice == 'paper':                                                                                       #if player 1 chose paper
        if p2_choice == 'rock':                                                                                      #if player 2 chose rock
            print(f"{p1_name} wins")                                                                                 #display message
            p1_score += 1                                                                                            #increment player 1 score
        elif p2_choice == 'scissors':                                                                                #if player 2 chose scissors
            print(f"{p2_name} wins")                                                                                 #display message
            p2_score += 1                                                                                            #increment player 2 score
        elif p2_choice == 'water':                                                                                   #if player 2 chose water
            print(f"{p2_name} wins")                                                                                 #display message
            p2_score += 1                                                                                            #increment player 2 score
    elif p1_choice == 'scissors':                                                                                    #if player 1 chose scissors
        if p2_choice == 'paper':                                                                                     #if player 2 chose paper
            print(f"{p1_name} wins")                                                                                 #display message
            p1_score += 1                                                                                            #increment player 1 score
        elif p2_choice == 'rock':                                                                                    #if player 2 chose rock
            print(f"{p2_name} wins")                                                                                 #display message
        elif p2_choice == 'water':                                                                                   #if player 2 chose water
            print(f"{p2_name} wins")                                                                                 #display message    
            p2_score += 1                                                                                            #increment player 2 score   
    elif p1_choice == 'water':                                                                                       #if player 1 chose water
        if p2_choice == 'rock':                                                                                      #if player 2 chose rock
            print(f"{p2_name} wins")                                                                                 #display message        
            p2_score += 1                                                                                            #increment player 2 score
        elif p2_choice == 'paper':                                                                                   #if player 2 chose paper
            print(f"{p1_name} wins")                                                                                 #display message                                     
            p1_score += 1                                                                                            #increment player 1 score                     
        elif p2_choice == 'scissors':                                                                                #if player 2 chose scissors                     
            print(f"{p2_name} wins")                                                                                 #display message                      
            p1_score += 1                                                                                            #increment player 1 score                

    print(f"{p1_name} score: {p1_score}, {p2_name} score: {p2_score}")                                               #display scores       
    
    if p1_score == score_limit:                                                                                      #if player 1 reached score limit    
        print(f"{p1_name}, reached", score_limit, "points and won the game!")                                        #display message
        break                                                                                                        #end forever loop                     
    elif p2_score == score_limit:                                                                                    #if player 2 reached score limit         
        print(f"{p2_name} reached", score_limit, "points and won the game. better luck next time!")                  #display message
        break

    play_again = input("do you want to play again? (yes/no): ").lower()                                              #prompt user to play again          
    value_choices = ['yes', 'no']                                                                                    #list of valid responses
    while play_again not in value_choices:                                                                           #input validation loop                          
            play_again = input("invalid input, please enter 'yes' or 'no': ").lower()                                #input validation        
    if play_again != 'yes':                                                                                          #if user does not want to play again                    
        break                                                                                                        #end forever loop
    continue                                                                                                         #continue forever loop         
                                                                                                        
print("final scores - player:", p1_score, "computer:", p2_score)                                                     #display final scores
print("thanks for playing!")                                                                                         #display message
print("""                                                                                                            
             ___________                                                                                             
            '._==_==_=_.'                                                                                            
            .-\:      /-.                                                                                            
           | (|:.     |) |                                                                                              
            '-|:.     |-'                                                                                            
              \::.    /                                                                                              
               '::. .'                                                                                                          
                 ) (                                                                                                 
               _.' '._                                                                                                  
              `"""""""`                                                                                              
""")                                                                                                                 #display message    
