import sys

def even(number):
    if number % 2 == 0:
        return("even")
    else:
        return("odd")

def collatz(number):
    while True:
        if even(number) == "even": 
            number = number/2
            return(number)
        elif even(number) == "odd":
            number = number * 3 + 1
            return(number)

def check_integer(number):
    try:
        number = int(number)
    except ValueError:
        return "wrong input"
    return number
    
def main():
    iterations = 0 
    while True:
        number = input("Enter a postitive number:")
        if number == "stop":
            sys.exit()
        elif check_integer(number) == "wrong input":
            print("You did not enter a number")
        else:
            number = check_integer(number)
            break
    while number != 1:
        number= collatz(number)
        iterations += 1
    print(iterations)

main()