from argparse import ArgumentParser
import sys
from datetime import date 
import time 
users_register = {
    "Federica": "TxelLci#2@8",
    "Irina_Bu": "Buhaniuc-irina",
}

parser = ArgumentParser(description="Will take as argument user-name and password in order to have acces to amazon's datebase")

parser.add_argument("user_name", type =str, help = "username")

parser.add_argument("password", type =str, help = "password")

args = parser.parse_args()

user_name = args.user_name
user_password = args.password
# function to validate password 
trys = 0
turn_verifyinputs_on = True
while turn_verifyinputs_on:
    print("Verifying, please wait...\n")
    time.sleep(2)
    for user in users_register:
        if user_name == user and users_register[user] == user_password:
            print("Registration succesful!")
            turn_verifyinputs_on = False
            break
        else:
            if trys == 2:
                print("Pleas register again!")
                sys.exit(1)
                turn_verifyinputs_on = False
            print("Incorrect Username or Password. Please try again!")
            print("Try again in 5 seconds")
            trys += 1
            time.sleep(1)
            
            user_password = input("Username: ")
            user_password = input("Password:")
            print("")

    

print("---------------------")
print("| Welcome to Amazon! |")
print("---------------------")

user_phone_number = input("Please enter phone number to continue: ")
# function to validate phone number 


