''' 
    flowerpot
    Name: Kaki Weiksner 
    Description: Determines the size of the box, and how much it will cost 
    Bugs: There are no bugs that I have found 
    Features: None
    Logs: 1.0 intial release 1150 
    Sources: W3 schools for lstrip 
'''
import sys              #imports the file sys 

def get_size(length, height,thickness):
    """
    Args: 
        height(float): The first number that the user entered and the height of their box 
        length(float): The second number that the user entered and the length of their box 
        thickness (float): The first number that the user entered and the height of their box 
    Retuns:
        str: the size of the box 
    """

    perimeter = length + 2 * height + 2 * thickness             #primeter is th length times the 2 times the height plus 2 times the length
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
        exit()              #exsits the code
    return size

def get_distance(zip):
    """
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
        exit()
    return zone

def get_cost(size,zone_distance):
    """"
    Args:
       size(int): The size of the box as a number
       perzone(int): The number of zipcode that packages will go through
    Returns:
        cost(int): The cost of the package. 
    Raises
    """
    #gets the cost of the package 
    if size == 1:
        cost = .03*zone_distance + .20
    elif size == 2: 
        cost = .03*zone_distance + .37
    elif size == 3:
        cost = .04*zone_distance + .37
    elif size == 4:
        cost = .05*zone_distance + .6
    elif size == 5: 
        cost = .25*zone_distance + 2.95
    elif size == 6: 
        cost = .35*zone_distance + 3.95
    else: 
        print("Something went wrong")
        exit()                                                                  #exist codes 
    return cost 

def main(): 
    while True: 
        data= input("Welcome to post office please eter Enter DATA (hieght, length, thickness, your staring zip code and the zipcode you are shipping too): ")          #has the user enter the sizes of the boxes
        data = data.split(",")                                   # splits the data that they entered after every comma

        #makes sure they only entered 5 things and then makes sure that the right type is entered
        if len(data)!= 5: 
            print("please enter 5 values")
        else:
            try: 
                height = float(data[0])                                      # height is the first thing that they enter 
                length = float(data[1])                                     # length is the second thing that they enter
                thickness= float(data[2])                                   # thickness he third thing that they enter
                starting_zip = int(data[3])                                # starting zip is the 4th thing that they enter
                ending_zip= int(data[4])                                  #starting zip is the 5th thing that they enter
                break
            except ValueError:
                print("You did not enter the correct information")       

    start_zip = get_distance(starting_zip)                              #gets the zone of the staring zip code 
    end_zip = get_distance(ending_zip)                                   #gets the zone of the ending zip code 
   
    #finds the number of zones the package is going through
    zone_distance = start_zip - end_zip                                        
    zone_distance = abs(zone_distance)                                             
    
    size= get_size(length, height,thickness)                            #calls the function with 3 args 
    
    cost = get_cost(size, zone_distance)                                     #calls the function with 2 args 
    cost = str(cost)                                                     
    cost = cost.lstrip("0")                                             #removes 0 from the begging of cost if there is one 
    print("Your cost is $", cost)                                         


main()          #displays the function main 
