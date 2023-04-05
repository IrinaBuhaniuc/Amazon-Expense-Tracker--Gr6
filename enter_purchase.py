# from 6 to ...
from argparse import ArgumentParser
import sys
import datetime
import time 
import re

purchases = []


def enter_purchase():
    user_purchase = {}
    #input the date
    while True:
        date_of_purchase = input("Enter the date of the purchase (MM/DD/YYYY or MM-DD-YYYY): ")
        if re.match(r"\d{2}/\d{2}/\d{4}", date_of_purchase):
            # if matches MM/DD/YYYY format, convert it to the desired format
            date_obj = datetime.datetime.strptime(date_of_purchase, "%m/%d/%Y")
            date_of_purchase = date_obj.strftime("%m/%d/%Y")
            break
        elif re.match(r"\d{2}-\d{2}-\d{4}", date_of_purchase):
            # if  matches MM-DD-YYYY format, convert it to the desired format
            date_obj = datetime.datetime.strptime(date_of_purchase, "%m-%d-%Y")
            date_of_purchase = date_obj.strftime("%m/%d/%Y")
            break
        else:
            print("Invalid date format. Please enter a date in MM/DD/YYYY or MM-DD-YYYY format.")
        # save the date to the purchases
    user_purchase["date"] = date_of_purchase
    
    # input the item purchased
    while True:
        item = input("Enter the item purchased: ")
        if isinstance(item,str) and len(item) >=3:
            user_purchase["item"] = item
            break
        else:
            print("Invalid item. Should be at least 3 characters")
    
    # input the total cost 
    while True:
        cost_string = input("Enter the cost of the item in Euro: ")
        try:
            cost = float(cost_string)
            user_purchase["cost"] = cost
            break
        except ValueError:
            print("Invalid cost. Should be a number (e.g., 10 or 12.50)")
            continue
    
    # input the weight
    while True:
        try:
            weight = float(input("Enter the weight of the item in kg: "))
            if isinstance(weight, float):
                user_purchase["weight"] = weight
                break
            else:
                print("Invalid weight. Should be a decimal number (e.g., 12.50)")
                continue
        except ValueError:
            print("Invalid weight. Should be a decimal number (e.g., 12.50)")
            continue
        
    # input the quantity
    while True:
        quantity_string = input("Enter the quantity of the item: ")
        try:
            quantity = int(quantity_string)
            if quantity >= 1:
                user_purchase["quantity"] = quantity
                break
            else:
                print("Invalid quantity. Should be more than 1")
                continue
        except ValueError:
            print("Invalid quantity. Should be an integer (e.g., 2)")
            continue
            
    purchases.append(user_purchase)

enter_purchase()
