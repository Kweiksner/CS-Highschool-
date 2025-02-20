'''
flowerbox
author; Kaki Weiksner
Date:2/11/25
despriction: Creating different functions in the string class 
bugs: none
sources: none
'''

import random

def reverse(word): 
    """"
    Description: puts the word in reverse
    Args:
       word(str): The word the user inter
    Returns:
        new_word(str): The word in reverse. 
    Raises:
        none
    """
    new_word = []
    for i in range(len(word)):
        new_word.insert(0, word[i])                             #adds the letter to beggining of the word
    new_word = (''.join(new_word))                            #delets paratheses
    return new_word

def see_vowels(word, vowels):
    """"
    Description:sees how many vowels are in a word
    Args:
       word(str): The word the user entered
       vowels(list): A list of all the vowels
    Returns:
        counter(int): The amount of vowels. 
    Raises:
        none
    """
    counter = 0
    for i in range(len(word)):
        if word[i] in vowels: 
            counter += 1
        else: 
            continue
    return counter

def see_consonants(word, vowels):
    """"
    Description:determines the number of consonents 
    Args:
        word(str): The word the user entered
        vowels(list): A list of all the vowels

    Returns:
        counter(int): The amount of connsonents. 
    Raises:
        none
    """
    counter = 0
    for i in range(len(word)):
        if word[i] not in vowels: 
            counter += 1

    return counter

def split_first_name(pieces):
    """
    Description:Finds first name
    Args:
        pieces(list):list of the first, middle, last name
    Returns:
        name(str): The first name 
    Raises:
        none
    """
    name = pieces[0]
    return name

def split_middle_name(pieces):
    """
    Description:Finds middle name 
    Args:
        pieces(list):list of the first, middle, last name
    Returns:
        middle_name(str): The middle name
    Raises:
        none
    """
    if len(pieces) > 2:
        middle_name = (pieces[1:-1])
        middle_name = (', '.join(middle_name))                      #delets paratheses
    else: 
        middle_name = ("none")

    return middle_name

def split_last_name(pieces):
    """
    Description:Finds last name 
    Args:
        pieces(list):list of the first, middle, last
    Returns:
        last_name(str): The last name 
    Raises:
        none
    """
    if len(pieces) > 1: 
        last_name = pieces[-1]
        return last_name
    else:
        return False

def bolean_name(name):
    """
    Description:determines if there is a hyphen
    Args:
        name(str):their name
    Returns:
        true:if there is a hyphen
        false: if there is not a hyphen
    Raises:
        none
    """
    #goes through each letter to see if it is a hyphen 
    for i in range(len(name)):                          
        if name[i] == "-": 
            return True
        else:
            continue
    return False

def lower_case(word):
    """
    Description:converts the word to lowercase
    Args:
        word(str):the word they entered
    Returns:
        new_word(str): the lowercase word
    Raises:
        none
    """
    new_word = []
    for i in range(len(word)):
        if ord(word[i]) >= 65 and ord(word[i]) <= 90:                       #if the ord is btw 65 and 90, the values for lowercase
            letter = chr(ord(word[i])+32)                                   #adds 32 to ord of the word
            new_word.append(letter)
        else:                                                               #if the charecter is not a letter
            new_word.append(word[i])
    new_word = ("".join(new_word))                                          #delets paratheses
    return new_word

def upper_case(word):
    """
    Description:converts the word to uppercase
    Args:
        word(str):the word they entered
    Returns:
        new_word(str): the uppercase word
    Raises:
        none
    """
    new_word = []
    for i in range(len(word)):
        if ord(word[i]) >= 97 and ord(word[i]) <= 122:                     #if the ord is btw 97 and 122, the values for uppercase
            letter = chr(ord(word[i])-32)                                  #adds 32 to ord of the word
            new_word.append(letter)
            new_word.append(letter)
        else:                                                              #if the charecter is not a letter
           new_word.append(word[i])
    new_word = ("".join(new_word))                                         #delets paratheses

    return new_word

def palindrome_checker(word): 
    """
    Description:determines if word is a palindrome
    Args:
        word(str):the word they entered
    Returns:
        true:if there is a palindrome
        false: if there is not a palindrome
    Raises:
        none
    """
    new_word=[]
    for i in range(len(word)): 
        if word[i] != " ":
            new_word.append(word[i])
    for i in range(len(new_word)):
        if new_word[i] == new_word[-i-1]:
            continue
        else:
            return False
    return True

def shuffle_word(word):
    """
    Description:shuffles the words
    Args:
        word(str):the word they entered
    Returns:
        New_word(str): the new word
    Raises:
        none
    """
    new_word = []
    old_word = []

    #adds each letter to old word
    for i in range(len(word)): 
        old_word.append(word[i])
    #picks a random word
    for i in range(len(word)):
        letter = random.choice(old_word)
        old_word.remove(letter)
        new_word.append(letter)
    new_word = ("".join(new_word))                                  #gets rid of paratheses
    return new_word

def initials(pieces): 
    """
    Description:Finds the initials
    Args:
        pieces(list):list of the first, middle, last name
    Returns:
        initial(str): the initials 
    Raises:
        none
    """
    initial = ''

    for name in pieces:
        initial += name[0].upper() + ". "
    return initial

def main():
    print('''
    1. Print Word in reverse 
    2. Determine Number of vowels 
    3. Determine Connsenants 
    4. First Name
    5. Second Name
    6. Last Name
    7. See if Last Name has a hyphen 
    8. Convert to Lowercase
    9. Conver to Uppercase
    10. Determine if word is a palindrome
    11. Suffle letters in word
    12.Determine Initials 
    ''')
    vowels = ["a", "e", "i", "o", "u", "y"]
    while True: 
        menu = input("Enter the number you want to run or quit if you want to quit")
        word = input("Enter word: ")

        if menu == "1": 
            print(reverse(word))
        elif menu == "2":
            lower_word = lower_case(word)
            vowels = (see_vowels(lower_word,vowels))
            print(vowels)
        elif menu == "3": 
            lower_word = lower_case(word)
            consonants_word = (see_consonants(lower_word,vowels))
            print(consonants_word)
        elif menu == "4":
            pieces = word.split(" ")
            first_name = split_first_name(pieces)
            print(first_name)
        elif menu == "5":
            pieces = word.split(" ")
            middle_name = split_middle_name(pieces)
            print(middle_name)
        elif menu == "6":
            pieces = word.split(" ")
            last_name = split_last_name(pieces)
            print(last_name)
        elif menu == "7": 
            last_name = split_last_name(word)
            hyphen = bolean_name(last_name)
            print(hyphen)
        elif menu == "8": 
            lowerword = lower_case(word)
            print(lowerword)
        elif menu == "9": 
            upperword = upper_case(word)
            print(upperword)
        elif menu == "10": 
            lower_word = lower_case(word)
            palindrome = palindrome_checker(lower_word)
            print(palindrome)
        elif menu == "11": 
            lower_word = lower_case(word)
            shuffle = shuffle_word(lower_word)
            print(shuffle)
        elif menu == "12": 
            pieces = word.split(" ")
            name_initials = initials(pieces)
            print(name_initials)
        elif menu == "quit": 
            break
        else: 
            print("You did not enter a value")

main()