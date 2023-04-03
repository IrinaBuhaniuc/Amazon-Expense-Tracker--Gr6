import re
from datetime import datetime 
import time



def enter_purchase(purchases):
    # The function will save the purchase details in a list of dictionaries
    #at the and will print("Purchase saved.") 
    purchase = {}
    enter_date = False
    while enter_date is not True:
        date_input = input("Enter the date of the purchase (MM/DD/YYYY): ")
        date_reg = re.search(r"\d\d(/|-)\d\d(/|-)\d\d\d\d", date_input)

        if date_reg is not None:
            date_of_purchase = date_reg.group()
            date_of_purchase = re.sub("-", "/", date_of_purchase)
            purchase["date"]= date_of_purchase
            enter_date = True
        else:
            print("Please enter a valid date.")
    print("...")
    time.sleep(1)
    purchased_item = input("Enter the item purchased: ")
    purchase["item"] = purchased_item
    print("...")
    time.sleep(1)
    cost_of_item = float(input("Enter the cost of the item in Euro: "))
    purchase["cost"]= cost_of_item
    print("...")
    time.sleep(1)
    weight_of_item = float(input("Enter the weight of the item in kg: "))
    purchase["weight"] = weight_of_item
    print("...")
    time.sleep(1)
    purchased_quantity = int(input("Enter the quantity purchased: "))
    if purchased_quantity >=1:
        purchase["quantity"] = purchased_quantity
    else:
        print("Please enter valid purchased quantity.")
    purchases.append(purchase)
    print("...")
    time.sleep(1)
    print("Purchase saved")
    