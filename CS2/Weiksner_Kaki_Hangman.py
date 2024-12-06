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
    
    
def check_guess(word):
  new_list = []
  for i in len(word): 
      new_list.append("_")
  print(new_list)
  #for index in len(word):
     # if word(index) == guess: 
         # print("hi")
            
                      

def main():
    lives = 7 
    word = ["kaki"]
    print("Welcome to Hangman")
    print(diagram(lives))
    while lives > 0: #loop for everything
        word = random.choice(word)
        go = 0 
        while go == 0: #loop to make sure that user entered a letter
            guess = input("Guess a letter: ")
            if guess.isalpha():
                    go = 1
            else:
              print("You did not enter a letter")
        if guess not in word: 
            lives = lives-1
            print("letter is not in word")
        else: 
            check_guess(word)
        print(diagram(lives))
            
main()


