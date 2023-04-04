# SKETCHES 

from argparse import ArgumentParser
import sys
from datetime import date 
import time 

users_register ={
    "Federica": "TxelLci#2@8",
    "Irina_Bu": "Buhaniuc-irina",
       }
purchases = [
    {
        "date": "01/04/23", # date of purchase 
        "item": "name", #item-name str with at least 3 characters 
        "cost": " 10",   # Cost of the item, including charges on delivery, should be float
        "weight": "1",  # The weight of the item( should be a float, and in kg)
        "quantity": "2", #The quantity purchased (should be an integer from 1 and above).
    }
]

def password_validator(string: str)->bool:
    # will return True if the password is valid 
    pass

def phoneNumberValidator(phone_number: str)->bool:
    # will return True if it is a valid german mobile number
    pass

def login(users_register: dict):
    #will return True if the username and password are correct
    # return username, password
    pass

    
def enter_purchase(purchases: dict):
    # The function will save the purchase details in a list of dictionaries
    #at the and will print("Purchase saved.") 
    pass

def generate_report(username: str,phone_number:str, purchases: dict): # will take information from dictionary 
    #will generate the report and will print it 
    pass 



# registration 

parser = ArgumentParser(description="Will take as argument user-name and password in order to have access to amazon's datebase")
parser.add_argument("user_name", type =str, help = "username")
parser.add_argument("password", type =str, help = "password")

args = parser.parse_args()

user_name = args.user_name
user_password = args.password

# function to validate password 
# if password is valid => registration successful done,
# Username and password are saved in users_register dictionary
 
if password_validator(user_password):
    users_register[user_name] = user_password



phone_num_validator = False 
while not phone_number_validator:
    phone_number = input("Please enter phone number to continue: ")
    # function for validating phone number, will return true or false 
    phone_num_validator = phoneNumberValidator(phone_number)
    


#Login
username = input("Username: ")
password = input ("Password: ")
if login(username, password):
    print("-------------------------------------")
    print("| Welcome to Amazon Expense Tracker! |")
    print("-------------------------------------") 
    
    print(f"Hello, {username}! Welcome to the Amazon Expense Tracker!")
    while option <3:
        print(f"What would you like to do?")
        print("1. Enter a purchase"
            "2. Generate a report"
            "3. Quit")
        option = int(input("Enter your choice (1/2/3): "))
        
        if option == 1:
            enter_purchase()
        elif option == 2:
            if option == 0:
                print("Please enter at least one purchase")
                break
            generate_report()
        elif option == 3:
            print("Quitting program...")
            time.sleep(2)
            print(f"Thank you for your visit, {username}. Goodbye!")
            sys.exit()     
        else:
            print("The operation you entered is not valid. Please select from the available options.")   
        
    

    










