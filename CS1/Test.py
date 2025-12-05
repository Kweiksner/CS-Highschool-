
import random                                                                                           #import the random library
import os                                                                                               #import the os library


def clear_screen():                                                                                     #define what clear_screen() does
    if os.name == 'nt':                                                                                 #if the program is running on a Windows machine
        os.system('cls')                                                                                #clear_screen() runs the window command to clear the terminal




choices = ['rock','paper','scissors']                                                                   #list possible choices
comp = 0                                                                                                #set variable 'comp', the computer's score, to 0
user1 = 0                                                                                               #set variable 'user1', the first user's score, to 0
user2 = 0                                                                                               #set variable 'user2', the second user's score, to 0


while True:                                                                                             #forever loop


    gamemode = input('Would you like to play with someone or computer? ').lower()                       #set gamemode as the response to the question 'Would you like to play with someone or computer?', turn response lowercase  
    if gamemode == 'someone':                                                                           #if the user response is 'someone'


        first = input('User1, Please enter a choice of rock, paper, or scissors: ').lower()             #set first as the response to 'User1, Please enter a choice of rock, paper, or scissors', turn response lowercase
        clear_screen()                                                                                  #clear the terminal
        second = input('User2, Please enter a choice of rock, paper, or scissors: ').lower()            #set second as the response to 'User2, Please enter a choice of rock, paper, or scissors', turn response lowercase
        clear_screen()                                                                                  #clear the terminal


        if first not in choices:                                                                        #if the first user's response does not match any item in the list
            print('User1 did not enter a valid response. Please try again.')                            #display 'User1 did not enter a valid response. Please try again.'
            continue                                                                                    #restart the loop


        elif second not in choices:                                                                     #otherwise if the second user's response does not match any item in the list
            print('User2 did not enter a valid response. Please try again.')                            #display 'User2 did not enter a valid response. Please try again.'
            continue                                                                                    #restart the loop


        print('User1 chose', first, 'and User2 chose', second)                                          #display 'User1 chose' and user1's response and 'User2 chose' and user2's response


        if first == second:                                                                             #if both users enter the same answer
            print('You tied!')                                                                          #display 'You tied!'
            print(f'Current score is {user1}:{user2}')                                                  #display 'Current score is' plus user1 score : user2 score


        elif (first == 'rock' and second == 'scissors' or \
              first == 'paper' and second == 'rock' or \
              first == 'scissors' and second == 'paper'):                                               #otherwise if user1 enters a winning response against user2
            print('User1 wins!')                                                                        #display 'User1 wins!'
            print(f'Current score is {user1 +1}:{user2}')                                               #display 'Current score is' plus user1 score +1 : user2 score
            user1 +=1                                                                                   #add 1 to the variable of user1's score
           
        else:                                                                                           #else
            print ('User2 wins!')                                                                       #display 'User2 wins!'
            print(f'Current score is {user1}:{user2 +1}')                                               #display 'Current score is' plus user1 score : user2 score +1
            user2 +=1                                                                                   #add 1 to the variable of user2's score


        again = input('Would you like to play again? ')                                                 #set again as the response to 'Would you like to play again?'
        if 'y' in again:                                                                                #if the letter y is in again
            continue                                                                                    #restart the loop
        else:                                                                                           #else
            print('Thank you for playing.')                                                             #display 'Thank you for playing.'
            break                                                                                       #end the loop


    else:                                                                                               #else if the user does not choose to play against someone else
            user_choice = input('Choose rock, paper, or scissors: ').lower()                            #set user_choice as the response to 'Choose rock, paper, or scissors', turn the response lowercase
            comp_choice = random.choice(choices)                                                        #ser comp_choice as a random choice from the list of choices




            if not any(item in user_choice for item in choices):                                        #if nothing in user_choice matches anything in the list                
                print ('You did not enter a valid response. Please try again. ')                        #display 'You did not enter a valid response. Please try again.'
                continue                                                                                #restart the loop


            elif user_choice == comp_choice:                                                            #otherwise if user_choice is the same as comp_choice    
                print('You tied!')                                                                      #display 'You tied!'                        
                print(f'Current score (comp:you) is {comp}:{user1}')                                    #display 'Current score (comp:you) is' plus comp:user1 variables  


            elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'paper' and comp_choice == 'rock') or \
         (user_choice == 'scissors' and comp_choice == 'paper'):                                        #otherwise if user_choice wins against comp_choice
                print(f'You chose {user_choice} and computer chose {comp_choice}. You win!')            #display 'You chose' plus user_choice and 'and computer chose] plus comp_choice and 'You win!'      
                print(f'Current score (comp:you) is {comp}:{user1+1}.')                                 #display 'Current score (comp:you) is' plus comp: user1 variable +1
                user1 += 1                                                                              #add 1 to the user1 variable                    


            else:                                                                                       #else if none of the above occur
                print(f'You chose {user_choice} and computer chose {comp_choice}. Computer wins!')      #display 'You chose' plus user_choice and 'and computer chose] plus comp_choice and 'Computer wins!'                                                
                print(f'Current score (comp:you) is {comp+1}:{user1}')                                  #display 'Current score (comp:you) is' plus comp +1 :user1 variables
                comp += 1                                                                               #add 1 to the comp variable
   


            again = input('Do you want to play again? ').lower()                                        #set again as response to 'Do you want to play again?', turn response lowercase
            if 'y' in again:                                                                            #if the letter 'y' is in again        
                continue                                                                                #restart the loop
            else:                                                                                       #else
                print('Thank you for playing.')                                                         #display 'Thank you for playing.'                        
                break                                                                                   #end the loop
