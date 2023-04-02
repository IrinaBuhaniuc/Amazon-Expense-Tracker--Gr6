import re
from datetime import datetime 
purchases = [
    {
        "date": "01/04/23", # date of purchase 
        "item": "name", #item-name str with at least 3 characters 
        "cost": " 10",   # Cost of the item, including charges on delivery, should be float
        "weight": "1",  # The weight of the item( should be a float, and in kg)
        "quantity": "2", #The quantity purchased (should be an integer from 1 and above).
    }
]


def enter_purchase():
    # The function will save the purchase details in a list of dictionaries
    #at the and will print("Purchase saved.") 
    purchase = {}
    date_input = input("Enter the date of the purchase (MM/DD/YYYY): ")
    date_reg = re.search(r"\d\d(/|-)\d\d(/|-)\d\d\d\d", date_input)
    date_of_purchase = date_reg.group()
    if date_reg is not None:
        date_of_purchase = re.sub("-", "/", date_of_purchase)
        purchase["date"]= date_of_purchase
        
    purchased_item = input("Enter the item purchased: ")
    purchase["item"] = purchased_item
    cost_of_item = float(input("Enter the cost of the item in Euro: "))
    purchase["cost"]=cost_of_item
    weight_of_item = float(input("Enter the weight of the item in kg: "))
    purchase["weight"] = weight_of_item
    purchased_quantity = int(input("Enter the quantity purchased: "))
    if purchased_quantity >=1:
        purchase["quantity"] = purchased_quantity
    else:
        print("Please enter valid purchased quantity.")
    purchases.append(purchase)
    print("Purchase saved.")
    

enter_purchase()