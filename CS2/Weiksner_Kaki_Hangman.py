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
    if lives == 5:
        print(''''
                +---+
                |   |
                o   |
                    |
                    |
                    |
              =======          
                ''')
    if lives == 4:
        print(''''
                +---+
                |   |
                o   |
                 \  |
                    |
                    |
              =======          
                ''')
    if lives == 3:
        print(''''
                +---+
                |   |
                o   |
               / \  |
                    |
                    |
              =======          
                ''')
    if lives == 2:
        print(''''
                +---+
                |   |
                o   |
              / | \ |
                |   |
                    |
              =======          
                ''')
    if lives == 1:
        print(''''
                +---+
                |   |
                o   |
              / | \ |
                |   |
               /    |
              =======          
                ''')
    if lives == 0:
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
    while play_again == "yes": 
        guessed_correctly = []
        lives = 6 
        word = ["kaki"]
        print("Welcome to Hangman")
        print(diagram(lives))
        word = random.choice(word)

        while lives > 0: #loop for everything
            go = 0 
            while go == 0: #loop to make sure that user entered a letter
                guess = input("Guess a letter: ")
                if guess.isalpha():
                        go = 1
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
                guessed_word = check_guess(guessed_correctly,word,guess)
                print(diagram(lives))
                print(guessed_word)
        
                if check_win(guessed_word):
                    continue
                else:
                    lives = 0

            print(f"You have {lives} left")
        play_again = str.lower(input("Would you like to play agin"))
        
        while True:
            if play_again == "no": 
                print("Have a good day")
                sys.exit()
            elif play_again == "yes":
                break
            else: 
                print("Enter Yes or no")


            
main()

