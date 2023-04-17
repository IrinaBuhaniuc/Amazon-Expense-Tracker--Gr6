from argparse import ArgumentParser
import sys
import os
import time 
from enter_purchase import enter_purchase
from password import password_validator
from report_generator import generate_report
from login import login
from phone_validator import phoneNumberValidator
from loading_dots import loading 

users_register ={}
purchases = [
    # {
    #     # "date": "01/04/2023", # date of purchase 
    #     # "item": "book", #item-name str with at least 3 characters 
    #     # "cost": 10,   # Cost of the item, including charges on delivery, should be float
    #     # "weight": 1,  # The weight of the item( should be a float, and in kg)
    #     # "quantity": 2, #The quantity purchased (should be an integer from 1 and above).
    # }
]

if __name__ == '__main__':
    # registration 

    parser = ArgumentParser(description="Will take as argument user-name and password in order to have access to amazon's datebase")
    parser.add_argument("user_name", type =str, help = "username")
    parser.add_argument("password", type =str, help = "password")

    args = parser.parse_args()
    
    if password_validator(args.password):
        users_register[args.user_name] = args.password
        print("\nRegistration successful!\n")



    #Login

    login_details = login(users_register)
    username = login_details[0]
    password = login_details[1]
    phone_number = phoneNumberValidator()
    
    os.system("clear")
    
    print("")
    print("--------------------------------------")
    print("| Welcome to Amazon Expense Tracker! |")
    print("--------------------------------------") 
    print("")
    time.sleep(1)


    option = ""
    if username and password:
        print(f"Hello, {username.capitalize()}! Welcome to the Amazon Expense Tracker!")
        while option != 1 or option != "2":
            loading()
            time.sleep(1)
            print(f"\nWhat would you like to do?")
            print("1. Enter a purchase\n"
                "2. Generate a report\n"
                "3. Quit")
            option = input("Enter your choice (1/2/3): ")

            if option == "1":
                os.system('clear')
                enter_purchase(purchases)
                print("\n Purchase saved.")
                time.sleep(2)
                os.system('clear')
                
            elif option == "2":
                if len(purchases) == 0:
                    time.sleep(1)
                    loading()
                    time.sleep(1)
                    os.system('clear')
                    print("Please enter at least one purchase")
                    continue
                os.system('clear')
                generate_report(username, phone_number, purchases)
                time.sleep(3)
            elif option == "3":
                loading()
                time.sleep(1)
                print("\nQuitting program", end = "")
                loading()
                time.sleep(1)
                print(f"\nThank you for your visit, {username.capitalize()}. Goodbye!")
                sys.exit()     
            else:
                print("Please enter a valid option number.")  

        










