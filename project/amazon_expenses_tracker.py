# SKETCHES 

from argparse import ArgumentParser
import sys
import time 
from purchases import enter_purchase
from report_generator import generate_report
from password import password_validator
from phone_number_validator import phoneNumberValidator
from login import login

users_register ={
    "Federica": "TxelLci#2@8",
       }

purchases = [
    {
        "date": "01/04/2023", # date of purchase 
        "item": "book", #item-name str with at least 3 characters 
        "cost": 10,   # Cost of the item, including charges on delivery, should be float
        "weight": 2,  # The weight of the item( should be a float, and in kg)
        "quantity": 2, #The quantity purchased (should be an integer from 1 and above).
    }
]


# registration 

parser = ArgumentParser(description="Will take as argument user-name and password in order to have acces to amazon's datebase")
parser.add_argument("user_name", type =str, help = "username")
parser.add_argument("password", type =str, help = "password")

args = parser.parse_args()

user_name = args.user_name
user_password = args.password


if password_validator(user_password):
    users_register[user_name] = user_password
    print("Registration successful!")

print(users_register)


#Login
login_details = login(users_register)
username = login_details[0]
password = login_details[1]
print("")
print("-------------------------------------")
print("| Welcome to Amazon Expense Tracker! |")
print("-------------------------------------") 
time.sleep(2)
print("")
#phone_number validation

phone_num_validator = False 
while not phone_num_validator:
    phone_number = input("Please enter phone number to continue: ")
    phone_num_validator = phoneNumberValidator(phone_number)


option = 0
if username and password:
    time.sleep(2)
    print("")
    print(f"Hello, {username.capitalize()}! Welcome to the Amazon Expense Tracker!")
    while option <3:
        print("...")
        time.sleep(2)
        print(f"What would you like to do?")
        print("1. Enter a purchase\n"
            "2. Generate a report\n"
            "3. Quit")
        option = int(input("Enter your choice (1/2/3): "))
        
        if option == 1:
            pass
            enter_purchase(purchases)
        elif option == 2:
            if option == 0:
                print("Please enter at least one purchase")
                break
            generate_report(username, phone_number, purchases)
            time.sleep(3)
        elif option == 3:
            print("...")
            time.sleep(1)
            print("Quitting program...")
            time.sleep(2)
            print(f"Thank you for your visit, {username.capitalize()}. Goodbye!")
            sys.exit()     
        else:
            print("Please enter a valid option number.")   
        
    

    











