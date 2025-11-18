import sys
#imports files from my computer 
import string 
import csv
import pandas as pd
import matplotlib.pyplot as plt

def iseven(number):
    if number % 2 == 0:
        return("even")
    else:
        return("odd")

def collatz(number):
    even = iseven(number)
    if even == "even": 
        number = number/2
        return(number)
    elif even == "odd":
        number = number * 3 + 1
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

def iterations(data):
    iterations = 0 
    ori_number = get_number()
    number = ori_number
    while number != 1:
        number= collatz(number)
        iterations += 1
    print(iterations)
    new_dictionary = add_dictionary(data,ori_number, iterations)
    create_graph(new_dictionary,ori_number, iterations)
    return new_dictionary

def add_dictionary(data_dict,number, iterations):
    data_dict[number] = iterations

def create_graph(data_dict):
    numbers = list(data_dict.keys())      # x-axis values
    iterations = list(data_dict.values())  # y-axis values

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(numbers, iterations, marker='o', linestyle='', markersize=8)

    # Add labels and title
    plt.xlabel('Number', fontsize=12)
    plt.ylabel('Iterations', fontsize=12)
    plt.title('Number vs Iterations', fontsize=14)

    # Add grid 
    plt.grid(True, alpha=0.3)

    # Display the plot
    plt.show()

def main():
    data = {}
       
    while True:
        iterations(data)
main()
