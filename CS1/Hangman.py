import random
hangman_pics = ['''
+---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
(  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = ["hello", "world", "python"]
#secret = random.choice(words)
secret = "hello"
print(secret)
secret_list = list(secret)
hidden = []
guesses = 0

for character in secret_list:
    hidden.append("_ ")
print("".join(hidden))

while guesses < len(hangman_pics)-1 and "_ " in hidden:
    guess = str.lower(input("Enter a letter: "))
    while True:
        guess = str.lower(input("Enter a letter: "))

        if guess in list("qwertyuiopasdfghjklzxcvbnm")
            print("Please enter a letter")
            break

    if guess in secret_list:
        for index in range(len(secret_list)):
            if guess == secret_list[index]:
                hidden[index] = guess
        print("".join(hidden))
    else:
        print("That letter is not here!")
        guesses += 1
        print(hangman_pics[guesses])

if guess >= len(hangman_pics)-1
    print("You lost")
else:
    print("You win!")
    
    





    

