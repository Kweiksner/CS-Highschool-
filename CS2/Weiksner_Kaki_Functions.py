'''
author; Kaki Weiksner
Date:2/211/25
despriction: Creating different functions in the string class 
bugs: none
sources:the election data assignment for the dictionary part, Mr Campbell, 
bonus:Menu, sorted array, title abrieviations, determines the frequency of connsonents
'''

import random
import sys

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

def consonants_frequency(word, consonants):
    """"
    Description:determines the number of consonents 
    Args:
        word(str): The word the user entered
        vowels(list): A list of all the vowels

    Returns:
        counter(int): The amount of connsonents. 
        sorted_words(dict): the frequency of all the consonants
    Raises:
        none
    """
    counter = 0
    frequency = dict()
    for i in range(len(word)):
        if word[i] in consonants: 
            counter += 1
            if word[i] not in frequency:                                     #if the letter is not in frequency yet
                frequency[word[i]]=1                                         #Sets the letter counter to 1
            else:
                frequency[word[i]] +=1                                       #adds one to letter counter
    sorted_words = dict(sorted(frequency.items(), key=lambda item: -item[1]))#sorts the dictionary by counter

    return counter, sorted_words

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

def sorted_array(word):
    """
    Description:puts letters in word in alphabetical order
    Args:
        word(str):the word the user entered
    Returns:
        new_letters(str):letters in alphabetical order
    Raises:
        none
    """
    numbers = []
    new_letters = []
    #transforms letters in to their ord number 
    for i in range(len(word)):
        letter= ord(word[i])
        numbers.append(letter)
        numbers.sort()
        
    #transforms the numbers into the corresponding letters 
    for i in range(len(numbers)):
        letters = chr(numbers[i])
        new_letters.append(letters)
    
    new_letters = ("".join(new_letters))                                          #delets paratheses
    return new_letters

def title_abbreviations(name,titles): 
    '''
    Description:determins if name has a title abbreviation
    Args:
        name(str):the word the user entered
        titles(list): list of possible titles
    Returns:
        True(bolean): if name has a abbreviation
        Flase(bolean): if name does not have an abreviation or is not long enough
    Raises:
        none
    '''
    if len(name) >= 3:                                                      # if the length of their name is 3 or more characters long
        if name[0:3] in titles:                                             #checks if an abbreviation is in the first three letters 
            return True
        elif name[0:2] in titles:
            return True
        else: 
            return False
    else:
        return False

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
    13. Sorted array name 
    14. Title abbreviations
    ''')
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x","z" ]
    titles = ["dr","esq","hon","jr","mr","mrs","ms","mmes","msgr","am","cao","ceo","cfo","cio","cisco","clo","cmo","coo","cpa","ba","bfa","bs","ma","mfa","ms","phd"]
    play =  "true"
    
    while play == "true": 
        game = "true"
        while game == "true":
            menu = input("Enter the number you want to run or quit if you want to quit: ")
            numbers = ["1","2","3","4","5","6","7","8","9","10","11","12","13", "14"]
            if menu == "quit": 
                print("Have a good day")
                sys.exit()
            elif menu not in numbers:
                print("You did not enter a valid term")
            else: 
                game = "false"

        word = input("Enter word or name: ")
        pieces = word.split(" ")
        lower_word = lower_case(word)
        last_name = split_last_name(word)


        if menu == "1": 
            print(reverse(lower_word))
        elif menu == "2":
            vowels = (see_vowels(lower_word,vowels))
            print(vowels)
        elif menu == "3": 
            consonants_word = (consonants_frequency(lower_word,consonants))
            print(consonants_word)
        elif menu == "4":
            first_name = split_first_name(pieces)
            print(first_name)
        elif menu == "5":
            middle_name = split_middle_name(pieces)
            print(middle_name)
        elif menu == "6":
            last_name = split_last_name(pieces)
            print(last_name)
        elif menu == "7": 
            hyphen = bolean_name(last_name)
            print(hyphen)
        elif menu == "8": 
            print(lower_word)
        elif menu == "9": 
            upperword = upper_case(word)
            print(upperword)
        elif menu == "10": 
            palindrome = palindrome_checker(lower_word)
            print(palindrome)
        elif menu == "11": 
            shuffle = shuffle_word(lower_word)
            print(shuffle)
        elif menu == "12": 
            name_initials = initials(pieces)
            print(name_initials)  
        elif menu == "13": 
            sortedarray = sorted_array(lower_word)
            print(sortedarray)   
        elif menu == "14":
            title = title_abbreviations(lower_word, titles)
            print(title)
        else: 
            print("You did not enter a value")

main()