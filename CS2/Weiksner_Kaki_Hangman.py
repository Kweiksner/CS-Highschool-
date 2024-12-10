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


def diagram(lives): 
    if lives == 7: 
        print(''''
                +---+
                |   |
                    |
                    |
                    |
                    |
              =======          
                ''')
    if lives == 6:
        print(''''
                +---+
                |   |
                o   |
              / | \ |
                |   |
              /   \ |
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
                  \ |
                    |
                    |
              =======          
                ''')
    if lives == 3:
        print(''''
                +---+
                |   |
                o   |
              /   \ |
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
              /     |
              =======          
                ''')
    if lives == 0: 
        print(''''
                +---+
                |   |
                o   |
              / | \ |
                |   |
              /   \ |
              =======          
                ''')
    else:
        print()
    
    
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
                new_list.append("_")
    return new_list
 
            
                      

def main():
    play_again = "yes"
    while play_again == "yes": 
        guessed_correctly = []
        lives = 7 
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
                    lives -= 1
                    print("You did not enter a letter")
            if guess not in word: 
                print("letter is not in word")
            else: 
                letters_guessed = check_guess(guessed_correctly,word,guess)
                print(letters_guessed)
            print(diagram(lives))
            print(f"You have {lives} left")
        play_again = str.lower(input("Would you like to play agin"))
        while True:
            if play_again == "no": 
                print("Have a good day")
            elif play_again == "yes":
                continue
            else: 
                print("Enter Yes or no")
                break


            
main()

