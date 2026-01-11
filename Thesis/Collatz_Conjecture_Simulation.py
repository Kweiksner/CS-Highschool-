import sys

def iseven(number):
    if number % 2 == 0:
        return("even")
    else:
        return("odd")

def collatz(number):
    even = iseven(number)
    if even == "even": 
        number = number/2
        print(number)
        return(number)
    elif even == "odd":
        number = number * 3 + 1
        print(number)
        return(number)

def check_integer(number):
    try:
        number = int(number)
    except ValueError:
        return "wrong input"
    return number

def get_number():
    while True:
        number = input("Enter a postitive number (Enter stop to stop code):")
        isinteger = check_integer(number)
        if number == "stop":
            sys.exit()
        elif isinteger == "wrong input":
            print("You did not enter a number")
        else:
            number = isinteger
            return(number)

def iterations():
    iterations = 0 
    number = get_number()
    while number != 1:
        number= collatz(number)
        iterations += 1
    print(iterations)
            
def main():
    while True:
        iterations()
main()

