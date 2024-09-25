'''
flowerpot
author; Kaki Weiksner
Date:4/17/14
despriction;This code has a wide variety of functions, some interactive with the user
bugs;none
sources; I used Ms Marcino, and Abanto to help. I also used W3 school and other websites to trouble shoot things I did not know how to do. 
challenges;Getting the initials of the last and first names, Reorginizing #5 and #6, have #6 work even if they do not put the numbers in order
'''



import random#the file random is imported into this program

def chorus ():#creates a function called chorus
    print('''Oh! Jingle bells, jingle bells
    Jingle all the way
    Oh, what fun it is to ride
    In a one-horse open sleigh, hey
    Jingle bells, jingle bells
    Jingle all the way
    Oh, what fun it is to ride
    In a one-horse open sleigh

    ''')#displays all of the text above

def song():#creates a function called song
    print('''Dashing through the snow
    In a one-horse open sleigh
    O'er the fields we go
    Laughing all the way
    Bells on bobtails ring
    Making spirits bright
    What fun it is to ride and sing
    A sleighing song tonight

    ''')

    chorus()#inserts the function, chorus

    print('''A day or two ago
    I thought I'd take a ride
    And soon, Miss Fanny Bright
    Was seated by my side
    The horse was lean and lank
    Misfortune seemed his lot
    He got into a drifted bank
    And then we got upsot
    See pop shows near Newark
    Get tickets as low as $194
    You might also like
    VULTURES
    ¥$, Kanye West & Ty Dolla $ign
    O Holy Night
    Christmas Songs
    Did you know that there’s a tunnel under Ocean Blvd
    Lana Del Rey

    ''')#displays all of the text above

    chorus()#inserts the function, chorus

    print('''A day or two ago
    The story I must tell
    I went out on the snow
    And on my back I fell
    A gent was riding by
    In a one-horse open sleigh
    He laughed as there I sprawling lie
    But quickly drove away

    ''')#displays all of the text above

    chorus()#inserts the function, chorus

    print('''Now the ground is white
    Go it while you're young
    Take the girls tonight
    And sing this sleighing song
    Just get a bobtailed bay
    Two forty as his speed
    Hitch him to an open sleigh
    And crack, you'll take the lead

    ''')#displays all of the text above

    chorus()#inserts the function, chorus

def addition(num1, num2):#creates a function called addition which takes in 2 parameters 
    print(f" Number 1: {num1}")#displays user for 1st number
    print(f" Number 2: {num2}")#displays user for 2ns number
    print(num1+num2)

def print_elements(my_list):#creates a function called print elements which takes in 1 parameters 
    for element in my_list:#goes through every element in each list
        print(element)#displays the elements 
        
def in_list(my_list, element):#creates a function called in list which takes in 2 parameters 
    if element in my_list:#if the element is in the list
        return True#displays to user True
    else:#anything else
        return False#displays false to user
    
def is_integer(parameter):#creates a function called integer which takes in 2 parameters 
    try:#sees if the parameter is an integer
       parameter = int(parameter)#turns the parameter into into an integer
       return True#displays true
    except ValueError:#if the parameter is not an integer
        return False#displays false

def get_integer(order):#creates a function called integer which takes in 2 parameters
    while True:#creates an infinate loop that can be stopped
        try:#sees if the parameter is an integer
            number = int(input(f"Number {order}: "))#aks user for 1st number
            return number#displays the nubmer
        except ValueError:#if the parameter is not an integer
            print("please enter a number!")#displays please enter a number

def generate_random_number():#creates a function called generate random number 
    while True:#creates an infinate loop that can be stopped
        numb1 = get_integer("1")#goes to the function get integer to get an integer
        numb2 = get_integer("2")#goes to the function get integer to get an integer
        
        if numb1 < numb2:#if number 1 is less than number 2
            print(random.randint(numb1,numb2))#displays a random number inbetween the the two that were imputted
            break#stops loop
        elif numb1 > numb2:#if number 1 is greater than number 2
            print(random.randint(numb2,numb1))#displays a random number inbetween the the two that were imputted
            break#stops loop
        else:#anything else
            print("Use two different numbers")#displays use two different numbers
def replace_character(string, old_ch, new_ch):#creates a function called replace characters which takes in 3 parameters 

    new_string = ""#starts a new string

    for ch in string:#looks at every letter in the sting one by one
        if ch == old_ch:#if the old character is the same as the cahracter that we are looking at
            new_string += new_ch#adds the letter to the new string
        else:#anything else
            new_string += ch#the character that it was looking at
    return new_string#displays the new word

def name_initials(name_first_initial, name_last_initial):#creates a function called name initials with 2 parameters
    name_1st_initial = name_first_initial[0]#the first initial is the first letter
    name_2nd_initial = name_last_initial[0]#the last name initial is the first letter in the last name
    print(name_1st_initial, name_2nd_initial)#displays the first and second initial 

def main():#creates a function called song
    song()#displays the function song
    print("Let's add 2 numbers")#displays lets add 2 numbers
    number1 = int(input("What is your first Number: "))#asks user ofr their first number
    number2 = int(input(f" What Number would you like to add to {number1}:"))#aks user for a second number to add to the first 
    addition(number1, number2)#puts the 2 numbers into the function addition
    numbers = ["1", "2", "3", "4","5"]#creates a list of 5 numbers
    print_elements(numbers)#puts the list into the function numbers and then displays it
    in_my_list = input("What number would you like to Check if it is in my list?")#asks the user for a number to try if it is in the list
    print(in_list(numbers, in_my_list))#inserts the list, numbers, and the number the computer is checking into the function in list
    parameter = input("Enter Parameter:")#asks user to enter a parameter
    print(is_integer(parameter))#inserts the parameter into the function integer
    print(generate_random_number())#displays the generate random number function
    string = input("What is your word")#asks user for their word
    new_chs = input("What would you like you like to replace")#asks the user what letter they want to replace
    old_chs = input("What is the letter that you would like to replace")# asks user what letter that they would like to replace
    print(replace_character(string, old_chs, new_chs))#inserts the word, and the letters they want to change and then prints the result of the function
    name_first = input("What is your name first name")#asks user for their first name 
    name_last = input("What is your name last name")#asks user for their last name
    print(name_initials(name_first,name_last))#inserts the first and last name into the function, name initials

main()#displays the function main






