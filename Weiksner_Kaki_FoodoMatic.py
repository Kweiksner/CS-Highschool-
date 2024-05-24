'''flowerpot
author; Kaki Weiksner
Date:10/27/23
description; This code allows the user to pick how many items they want to order and then ramdomly chooses what meal they will be having and a side that comes along with it. As well as what allergies the user should look out for. The code also caculates the cost of the meal. 
bugs;none
challenges;I used while true statements if the user answered a question the right way. I aslo made it so no matter if they typed it in lowercase or upper case the same thing happend. 
'''

import random#imports the file random
import sys#imports the fils sys 

bakery_items = ["Chocolate Chip Muffin", "Banana Muffin", "Popysead Muffin", "Choclate-Chip Cookie", "M and M Cookie", "Plain Crossiant", "Chocolate Crossiant"]#creates a list of all of the bakery iteams
bakery_items_allergies = ["Weat, Soy, Dairy, Choclate","Weat, Soy, Dairy, Banana", "Weat, Soy, Dairy, Popyseads", "Weat, Soy, Dairy,Choclolate", "Weat, Soy, Dairy, Choclate", "Weat, Soy, Dairy", "Weat, Soy, Dairy, Chocolate"]#creates a list of all of the ingreedents the Baked Goods
bakery_items_costs = [2.50,2.50,2.50,3.00, 3.00,4.00, 4.00]#creates a list for all of the cost for the items 
descriptors = ["Tomato and Mozzarella", "Acai", "Ham and Cheese", "Greenhouse", "Cobb"]#creates a list for all of the main courses
meals = ["Sandwich", "Bowl", "Crossaint", "Salad", "with Crackers"]#creats a list for all of the main items

print("Welcome to the Random Cafe, where you chose how many items you want, and we radomly pick what you will get.")#displays Welcome to the cafe

while True:#while the codition is true, the loop goes on forever
    number_of_items = input("How many items do you want to order? ")#asks user how many items they would like to order and the enter an answer

    try:#sees if number of items is an integer or not
        number_of_items = int(number_of_items)

        if number_of_items > 0:#if the number of items is greater than 0 
            break#breaks infinate loop
        else:#everything else
            no_food = str.lower(input("Are you sure that you do not want any food? "))#asks user if they are sure that do not want any food
            
            if no_food == "yes":#if the users answer to no food is yes
                print("I'm sorry that you do not want anything, you are really missing out, have a good day")#displaysI'm sorry that you do not want anything, you are really missing out, have a good day
                sys.exit()#exits the code
    except ValueError:#if the user did not input a number for number or items is not a number
        print("Please enter a valid integer!")#displays please enter a valid integer

total_cost = 0#sets the total cost to 0

for i in range(number_of_items): #goes through number of iterations that is the same as the number of items that they want to order
    bakery_item = random.choice(bakery_items)#picks a random item from the bakery_item list
    item_cost = bakery_items_costs[bakery_items.index(bakery_item)]# matches up the random bakery from before with the price using indexes
    allergies = bakery_items_allergies[bakery_items.index(bakery_item)]#matches up the random bakery from before with the allergies using indexes 
    print(f"\n{random.choice(descriptors)} {random.choice(meals)} with a {bakery_item}, which will cost ${item_cost}0. This meal contains {allergies}")#dispays a radom descripter with a radom meal, bakery item, and its correspoding allergy, and price
    total_cost += item_cost#adds the costs of each item they are ording
print(f"\n Your total cost is ${total_cost}0")# displays the final cost of their order
print("Have a good day")



