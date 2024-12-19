'''
Algo 
Set lives
Create Word
Create Diagram 
function
Get Guess
Check for existence 
Put it in sport 
Tries left 
Can the person guess the word(not necessary) 
Check win 
Check word function
Play again

FlowerBox 
Name: Kaki Weiksner 
Description: allows tow players to play hangman
Bugs: None that I have found
Feautures: User can play against someone else or the computer, computer picks a random word through a dictionary
Logs: 1.0 intial release 1150 
Sources: Mr Cambell https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/
'''

import random
import sys
import requests as rq
import os

def diagram(lives): 
    """
    Args: 
        lives(int): The number of lives a player has remaining 
    Retuns:
        viod: nothing
    """
    #based of the number of lives prints a board
    if lives == 6: 
        print(''''
                +---+
                |   |
                    |
                    |
                    |
                    |
              =======          
                ''')
    elif lives == 5:
        print(''''
                +---+
                |   |
                o   |
                    |
                    |
                    |
              =======          
                ''')
    elif lives == 4:
        print(''''
                +---+
                |   |
                o   |
                 \  |
                    |
                    |
              =======          
                ''')
    elif lives == 3:
        print(''''
                +---+
                |   |
                o   |
               / \  |
                    |
                    |
              =======          
                ''')
    elif lives == 2:
        print(''''
                +---+
                |   |
                o   |
              / | \ |
                |   |
                    |
              =======          
                ''')
    elif lives == 1:
        print(''''
                +---+
                |   |
                o   |
              / | \ |
                |   |
               /    |
              =======          
                ''')
    elif lives == 0:
        print(''''
                +---+
                |   |
                o   |
              / | \ |
                |   |
               / \  |
              =======          
                ''')

    else:
        print()

    
def check_win(guessed_word): 
    """
    Args: 
        guessed_word(list): The word that they guessed
    Retuns:
       True: If they one
    """
    #checks to see if there is any / in the words
    for i in range(len(guessed_word)):
        if guessed_word[i] == "/":
            return True

def check_guess(guessed_correctly,word, guess):
    """
    Args: 
        guessed_correctly(list): The letters that they have guessed correctly in previous turns
        word(str):The Word the user is trying to get 
        guess (str): The letter they guess 
    Retuns:
        new_list(list): The list of their guess so far
    """
    new_list = []
    #if the guess in the word it adds it to the new list, and it not it adds a / 
    for i in range(len(word)): 
        letter = word[i]
        if letter == guess:
            new_list.append(guess)
            guessed_correctly.append(guess)
        else:
            if letter in guessed_correctly:
                new_list.append(letter)
            else:
                new_list.append("/")
    return new_list
 
            
                      

def main():
    play_again = "yes"                                                                              #sets play again to yes
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","x","y","z"]
    while play_again == "yes":                                                                      #while the user still wants to play
        guessed_correctly = []                                                                      #creates a list for the letters they have guessed correctly
        guessed_letters = []                                                                            #creates a list for the letters they have guessed 

        lives = 6                                                                                    #sets lives to six
        print("Welcome to Hangman")
        diagram(lives)                                                                              #calls the board with one parameter

        while True:
            players = str.lower(input("Would you like to play against the computer"))               #asks user if they want to play against the computer
            
            if players == "no":                                                                     #if user wants to play against a friend
                while True: 
                    word = str.lower(input("player one enter word"))                                    #asks what their word is 
                    if word.isalpha(): 
                        os.system('cls')
                        break 
                    else: 
                        print("You must enter letters")
                break
            
            #if user wants to play against computer 
            elif players == "yes":
                word_list= []                                                                       #creates an empty list
                fhand = open('Weiksner_Kaki_dictionary.txt')                                        #opens the dictionary 
                #goes through each word and adds it to a list
                for word in fhand:                                                                  
                    word_list.append(word)
                word = random.choice(word_list)                                                     #picks a random word 
                word = word.strip()                                                                 #removes all extra spaces
                break
            else:
                print("Enter Yes or No")

        while lives > 0:                                                                    #loop for everything
            go = 0 
           
            while go == 0:                                                                  #loop to make sure that user entered a letter
                guess = str.lower(input("Guess a letter: "))                                #asks user to guess a letter
                #checks if the letter is in the alphabet
                if guess in alphabet:                                                       
                    go = 1
                else:
                    print("You did not enter a letter")
            
            #checks to see if the guess has already been guessed and is in the word 
            if guess in guessed_letters: 
                print("you already guessed that letter")
            elif guess not in word: 
                print("letter is not in word")
                lives -= 1
                print(diagram(lives))
                guessed_letters.append(guess)                                                   #adds the letter to guess letters
            else: 
                guessed_letters.append(guess)
                guessed_word = check_guess(guessed_correctly,word,guess)                       
                print(diagram(lives))
                print(guessed_word)
                print(lives)


                #calls the function to see if they one
                if check_win(guessed_word):
                    continue
                else:
                    lives = 0

            print(f"You have {lives} left")
        print(f"the word is {word}")
        
        while True:
            #Asks user if they want to play again
            play_again = str.lower(input("Would you like to play agin"))
            if play_again == "no": 
                print("Have a good day")
                sys.exit()                                                          #exsits the code
            elif play_again == "yes":
                break
            else: 
                print("Enter Yes or no")


            
main()

