''' 
    flowerpot
    Name: Kaki Weiksner 
    Description: Determins the size of the box, and how much it will cost 
    Bugs: 
    Features:
    Logs:
    Sources:
'''
import sys
def get_size(length, height,thickness):
    """
    Args: 
        hieght(float): The first number that the user entered and the hieght of their box 
        length(float): The second number that the user entered and the length of their box 
        thickness (float): The first number that the user entered and the hieght of their box 
    Retuns:
        str: the size of the box 
    """

    perimeter = length + 2 * height + 2 * thickness             #primeter is th length times the 2 times the height and 2 times the length
    #Finds the size of the box
    if height >= 3.5 and height <= 6 and length >= 3.5 and length <=4.25 and thickness >= .007 and thickness <=.015:
        size = 1
    elif height >= 3.5 and height <= 11.5 and length >= 4.25 and length <=6 and thickness >= .007 and thickness <=.015:
        size = 2
    elif height >= 5 and height <= 11.5 and length >= 3.5 and length <=6 and thickness >= .016 and thickness <=.25:
        size = 3
    elif height >= 11 and height <= 18 and length >= 6.125 and length <=24 and thickness >= .25 and thickness <=.5:
        size = 4
    elif perimeter <= 84:
        size = 5
    elif perimeter <=130 and perimeter >= 84:
        size = 6
    else:
        print("This item does not conform to any of the above requirement")
        exit()
    return size

def get_distance(zip):
    """"
    Args:
       zip(int): Either the staring zipcode or the end zip code 
    Returns:
        zone(int): The zone of either the starting or end zip code 
    """
    #gests the zone of the zip code 
    if zip >= 1 and zip <= 6999:
        zone = 1 
    elif zip >= 7000 and zip <= 19999:
        zone = 2
    elif zip >= 20000 and zip <= 35999:
        zone = 3
    elif zip >= 36000 and zip <= 62999:
        zone = 4 
    elif zip >= 63000 and zip <= 84999:
        zone = 5
    elif zip >= 85000 and zip <= 99999:
        zone = 6 
    else:
        print("You did not enter a valid zip code to ship from")
    return zone
def get_cost(size,perzone):
    """"
    Args:
       size(int): The size of the box as a number
       perzone(int): The number of zipcode that packages will go through
    Returns:
        cost(int): The cost of the package. 5
    Raises
    """
    #gets the cost of the package 
    if size == 1:
        cost = .03*perzone + .20
    elif size == 2: 
        cost = .03*perzone + .37
    elif size == 3:
        cost = .04*perzone + .37
    elif size == 4:
        cost = .05*perzone + .6
    elif size == 5: 
        cost = .25*perzone + 2.95
    elif size == 6: 
        cost = .35*perzone + 3.95
    else: 
        print("Something went wrong")
    return cost 

def main(): 
    while True: 
        data= input("Welcome to post office please eter Enter DATA (hieght, length, thickness, your staring zip code and the zipcode you are shipping too): ")#has the user enter the sizes of the boxes
        dimensions = data.split(",")                                   # splits the data that they entered after every comma
        
        #Makes sure only numbers are entered  
        for element in data:
            if element .isalpha():
                data = input("Please enter numbers only")
            else:
                break 
        #makes sure they only entered 5 things and then makes sure that the right type is entered
        if len(dimensions)!= 5: 
            print("please enter 5 values")
        else:
            try: 
                height = float(dimensions[0])                                      # height is the first thing that they enter 
                length = float(dimensions[1])                                     # length is the second thing that they enter
                thickness= float(dimensions[2])                                   # thickness he third thing that they enter
                starting_zip = int(dimensions[3])                                # starting zip is the 4th thing that they enter
                ending_zip= int(dimensions[4])                                  #starting zip is the 5th thing that they enter
                break
            except ValueError:
                print("You did not enter a number for the zipcodes")                               # ending zip is the 5th thing that they enter

    start_zip = get_distance(starting_zip)                              #gets the zone of the staring zip code 
    end_zip = get_distance(ending_zip)                                   #gets the zone of the ending zip code 
    perzone = start_zip - end_zip                                        #finds starting and ending zipcode distance
    perzone = abs(perzone)                                              #gets the aboslute value of perzone 
    size= get_size(length, height,thickness)                            #calls the function with 3 args 
    cost = get_cost(size, perzone)                                     #calls the function with 3 
    cost = str(cost)
    cost = cost.lstrip("0")                                             #removes 0 from the begging of cost if there is one 
    print("Your cost is", cost)                                         


main()#displays the function main 
#lstrip function to get rid of zeros 