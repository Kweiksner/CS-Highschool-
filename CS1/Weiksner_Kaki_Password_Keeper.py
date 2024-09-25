
'''
author; Kaki Weiksner
Date:5/09/24
Description: This code allows the user to enter passwords and stores them
bugs:none
sources: I used Ms Marcino, and Mr Abanto to help. I also used W3 school and other websites to troubleshoot things I did not know how to do. 
challenges: Can keep going, Put as many passwords as user wants, allows the user to change their passwords, see if strings are integers where they are supposed to be integers,asks user if there password is right or wrong, if user does enter the right thing for a sting it tells them to do it again
'''
import sys 

print("Password Keeper")#displays password keeper

def website_username_password(usernames,passwords,webistes):#creates a functions called website username, password with no parameters
    '''DESCRIPTION
    Asks user for usernames, passwords and websites and adds them to the list. Also chekcs if it is right or wrong. 
    Args:
        parameter names (usernmaes, passwords,websites): the lists that the usernames or websites or passwords will be added on too 
        usernames (list): A list of all of the usernmes
        passwords(list):A list of all of the passwords
        websites(list):A list of all of the websites 
    Prints:
        all of the websites, usernames and passwords
        try to put your infromation again: if they did not answer the correct question above
    '''
    while True:
        website = input("Enter Website: ")#asks user to enter website
        username = input(f"Enter Useraname for {website}")#asks user to enter username
        password = input(f"Enter Password for {website}")#asks user to enter password
        print(website)
        print(username)
        print(password)
        right_wrong = right_or_wrong()
            
        if right_wrong:
            passwords.append(password)#adds the 1st password to the list passwords
            usernames.append(username)#adds the 1st username to the list usernames
            websites.append(website)#adds the 1st website to the list websites
            break
        else:
            print("Try to put in your information again")

def see_integer(number):#creates a function called integer which takes in 2 parameters
    '''DESCRIPTION
    sees if a number is an integer 
    Args:
        number(str): a string that was entered to see if it is a number
    Returns:
        True(Bolean): if the the input is a number
        False(Bolean): if the input is not a number
    '''
    try:
        user_input = int(number)
        return True
    except ValueError:
        return False
    

def find_password(websites,usernames,passwords):#creates a function called find password with no parameters
    '''DESCRIPTION
    finds the password for a to whatever the user wants using the index
    Args:
        parameter names (usernmaes, passwords,websites): the lists that the usernames or websites or passwords will be added on too 
        usernames (list): A list of all of the usernmes
        passwords(list):A list of all of the passwords
        websites(list):A list of all of the websites 
    Prints:
        the website, username, and password
        enter a website that you have already entered: if the user did not enter the right thing in the question before
    '''
    while True: 
        web = input("Which website would you like to find the Passord to")#asks user which website they want to find
        if web in websites:
            user = usernames[websites.index(web)]#finds the index of usnernames 
            passw = passwords[websites.index(web)]#finds the index of passwords
            print(f" Website: {web} Username: {user} Password: {passw}")#displays the websites, username, and password
            break
        else:
            print("enter a website that you have already entered")

def change_password(websites,usernames,passwords):#creates a function called change password with no parameters
    '''DESCRIPTION
    allows the user to change the password
    Args:
        parameter names (usernmaes, passwords,websites): the lists that the usernames or websites or passwords will be added on too 
        usernames (list): A list of all of the usernmes
        passwords(list):A list of all of the passwords
        websites(list):A list of all of the websites 
    Prints:
        the new website, username and password
        Please enter username or password: if they did not enter that in the question above
    '''
    while True:
        old_website_change = str.lower(input(f"Which Website would you like to change the to? "))#aks what website they want to change the password
        if old_website_change in websites:
            while True:
                change_username_password = input("Would you like to change the username,or password")

                if change_username_password == "password":#if user enter password
                    passwords[websites.index(old_website_change)] = input("What is your new password")
                    break
                elif change_username_password == "username":
                    usernames[websites.index(old_website_change)] = input("What is your new username")
                    break
                elif change_username_password == "both":
                    usernames[websites.index(old_website_change)] = input("What is your new username")
                    passwords[websites.index(old_website_change)] = input("What is your new password")
                    break
                else:
                    print("Please enter username or password")
            break
            
        else:
            print("Please enter a website that you have already inputted")
def right_or_wrong():
    '''DESCRIPTION
    sees if the username, password, or website was right that was entered
        Returns:
            True(Bolean): if there password was right
            False(Bolean: If ther password was wrong
    Prints:
            Enter yes or no if they did not answer the question right 
    '''
    while True:
        is_right_password = str.lower(input("Is this the right Password"))
        if is_right_password == "no":
            return False
            break
        elif is_right_password =="yes":
            return True
            break
        else:
            print("Enter Yes or No")
        
        
def main():#creates a funtions called main
    websites = []#creates an empty list to store websites in
    usernames = []#creates an empty list to store usernames in
    passwords = []#creates an empty list to store passwords in

    while True:#creates infinite loop
        while True:
            times = input("How many passwords would you like to enter: ")#asks user how many passwords they want to enter
            if see_integer(times):
                break
            else:
                print("Enter a number")

        times = int(times)#converts time into an integer
        for i in range(times):#however many times the user puts in
            website_username_password(usernames,passwords,webistes)#prints the function website, uswername, password

        while True:
            mode = str.lower(input("Which would you like to do, change, display all or find one, or add"))
            if mode == "display all":
                for i in range(times):#however many times the user puts in
                    print(f"Website: {websites[i]}, username: {usernames[i]}, password: {passwords[i]}")#displays the websites, usernames and passwords
           
            elif mode == "find one":
                find_password(websites,usernames,passwords)#displays the function find password

            elif mode == "change":
                while True: 
                    times_change_password = input("How many passwords would you like to change")#asks user how many passwords they want to change
                    if see_integer(times_change_password):
                        times_change_password = int(times_change_password)#converets the times change password into an integer
                        for i in range(times_change_password):#repeats everything under this the number of times the user entered
                            print(change_password(websites,usernames,passwords))#displays the function change password 
                    else:
                        print("Enter a number")
                break
            else:
                print("Find one, change or display all")
  
        while True:
            stop = str.lower(input("Would you like to stop or keep going"))#asks user if they would like to stop or keep going
            if stop == "stop":#if user enter stop
                sys.exit()#exit the code
            elif stop == "keep going":
                break
            else:
                print("enter keep going or stop")
                
main()#displays the function main


