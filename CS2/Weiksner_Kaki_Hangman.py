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

'''
import random
import sys
import requests as rq

def diagram(lives): 
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

    for i in range(len(guessed_word)):
        if guessed_word[i] == "/":
            return True

def check_guess(guessed_correctly,word, guess):
    new_list = []
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
    guessed_letters = []
    play_again = "yes"
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","x","y","z"]
    while play_again == "yes": 
        guessed_correctly = []
        lives = 6 
        print("Welcome to Hangman")
        diagram(lives)

        while True:
            players = str.lower(input("How many players would you like to play against the computer"))
            if players == "no": 
                word = str.lower(input("player one enter word"))
                for i in range(40):
                    print()
                break
            elif players == "yes":
                url = 'https://www.mit.edu/~ecprice/wordlist.10000'
                word_list = rq.get(url).text.split()
                word = random.choice(word_list)
                break
            else:
                print("Enter Yes or No")

        while lives > 0: #loop for everything
            go = 0 
            while go == 0: #loop to make sure that user entered a letter
                guess = str.lower(input("Guess a letter: "))
                if guess in alphabet:
                    go = 1
                #if guess(len(range)) == 1:
                    #go =1
                else:
                    print("You did not enter a letter")
            
            if guess in guessed_letters: 
                print("you already guessed that letter")
            elif guess not in word: 
                print("letter is not in word")
                lives -= 1
                print(diagram(lives))
                guessed_letters.append(guess)
            else: 
                guessed_letters.append(guess)
                guessed_word = check_guess(guessed_correctly,word,guess)
                print(diagram(lives))
                print(guessed_word)
                print(lives)
        
                if check_win(guessed_word):
                    continue
                else:
                    lives = 0

            print(f"You have {lives} left")
        print(f"the word is {word}")
        
        while True:
            play_again = str.lower(input("Would you like to play agin"))
            if play_again == "no": 
                print("Have a good day")
                sys.exit()
            elif play_again == "yes":
                break
            else: 
                print("Enter Yes or no")


            
main()

