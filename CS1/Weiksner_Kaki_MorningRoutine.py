'''flowerpot
author; Kaki Weiksner
Date:10/27/23
despriction;This code asks the user questions that determins how their morning routine will go. 
bugs;none
challenges;I used while true statements if the user answered a question the right way. I aslo made it so no matter if they typed it in lowercase or upper case the same thing happend. 
'''

print('''Kaki's Morning Routine

Wake up''')

while True:#infinite loop (while condition True is true)
    weather = str.lower(input("Is it warm or Cold? "))#prompts user to answer whether it is warm or cold and converts it to lowercase letters if needed.

    if weather == "warm":
        print("I love the warm weather")#if the weather is warm,it prints I love warm weather. 

        while True:#start of loop 
            clothing_warm = str.lower(input("Do you want to wear a skirt and shorts? "))#asks user what you want to weat and converts it to lowercase letters. 

            if clothing_warm == "skirt":
                 print("Wear a skirt with a nice shirt")#if it is warm and you want to wear a skirt then it prints weat a skirt with a nice shirt. 
                 break#if the answer is skirt breaks loop.
            elif "short" in clothing_warm:
                print("Wear a Shirt with your shorts.")#if wants to wear shorts than it displays wear a shirt with your shorts
                break#if the answer is short breaks loop 
            else:
                print("I think you typed the wrong input,try again")#if anything else is imputting then it displays you typed the wrong input try again and then goes back to the begginning of the loop
        break# if answer to whats the weather is warm then it breaks the loop
    elif weather == "cold": 
        print("Remember to wear lots of layers")#if the weather is cold then it displays remember to wear lots of layers

        while True:#start of loop 
            clothing_cold = str.lower(input("Do you want to wear sweatpants of leggins? "))# asks if its cold do you want to wear sweatpants or leggins and converts it to lowercase letters. 

            if clothing_cold == "sweatpants":
                print("Wear a hoddie with your sweatpants")#if it is cold and user wants to wear sweatpants, then displays wear a hoodie with your sweatpants
                break#if answer is sweatpants than breaks loop
            elif clothing_cold == "leggins":
                print("Wear a sweater with your leggins.")#if  it is cold and user wants to wear leggins, then displays wear a sweater with your leggins
                break#if answer is leggins than breaks loop
            else:
                print("I think you typed the wrong input,try again")#if anything else is imputting then it displays you typed the wrong input try again and then goes back to the begginning of the loop
        break#breaks loop if answer to the weather is cold 
    else:
        print("I don't think you answered the question.")#if anything else is imputted then it starts the loop over again and displays I don't think you answered the question

print("Now that your dressed, it is time to eat breakfast")#displays this after the questions above are asnwered. 

while True:#start of loop 
    breakfast = str.lower(input("Do you want breakfast today? "))#asked user do you want breakfast today
    if breakfast == "yes":
        print("Yummmmmmmm, Eat whatever your Mom made you this morning")#if answer is yes it displays yumm eat whatever your mom made you this morning
        break#if answer is yes it breaks loop
    elif breakfast == "no":
        print("Remember that breakfast is the most important meal of the day and you will be hungry later?")#if the answer to breakfast is no then it displays remember to eat breakfast because it is the most important meal of the day. 
        while True:#start of loop 
            sure = str.lower(input("Are you sure?"))#asks user are you sure
            if sure == "no":
               print( "I'm glad that you changed your mind and that you want to eat.")#if answer is no than it displays i'm glad you changed your mind.
               break#breaks loop if answer is no
            elif sure == "yes":
                print("I'm sorry that you are not hungry, but remember to eat a good lunch")#if answer is yes then it displays, I'm sorry that you are not hungry, but remember to eat a good lunch
                break#breaks loop if answer is yes
            else:
                print("I didn't understand your answer, try again")#if answer is anything else than it displays I didn't understand your answer, try again and then it starts the loop over again. 
        break #breaks loop if the answer is no to breakfast
    else:
        print("Remember to answer yes or no")#if anything else is imputted than it displays, remember to answer yes or no and starts the loop over again

while True:#start of loop 
    brushteeth = str.lower(input("Have you brushed your teeth yet? "))#asks the suer if they have brushed their teeth or not and then converts the answer into lowercase letters

    if brushteeth == "yes":
        print("Great, remember to this everyday")#if user has brushed their teeth, then displays greatm remeber to this everyday. 
        break#breaks code if answer to question is yes
    elif brushteeth == "no":
        print("Go and brush your teeth")#if user imputs no then it displays go and brush your teeth and then repeats loop

    else:
        print("Rember to answer yes or no")#if user imputs anything else it prints remeber to answer yes or no and then repeats loop

while True:#start of loop 
    pack = str.lower(input("Have you packed your bag yet? "))# asks user if they have packed their bag yet and then converts it into lowercase letters

    if pack == "yes":
        print("Great, now it is time to go to school.")#if the answer is yes then it prints great, now it is time to go to school
        break#breaks loop if the answer is yes
    elif pack == "no":
        print("Go and back your bag")#if the answer is no, then it displays go and pack your bag and then starts the loop over again. 
    else:
        print("Rember to answer yes or no")#if the answer is anything else then it prints remember to answer yes or no and then starts the loop over again





