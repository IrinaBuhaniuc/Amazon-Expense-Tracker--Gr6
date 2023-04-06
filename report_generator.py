from datetime import datetime, date
import time
def generate_report(name,phone_number, purchases):
    def most_expensive_item(list):
        max = 0
        for dict in list:
            for key in dict:
                if dict[key] > max:
                    max = dict[key]
                    max_item_name = key
        return max_item_name, max

    def least_expensive_item(list):
        min = float('inf')
        for dict in list:
            for key in dict:
                if dict[key] < min:
                    min = dict[key]
                    min_item_name = key
        return min_item_name, min
              
    password = "***"
    if phone_number[0] == "+":
        stars_phone_number = "+49" + "***" + phone_number[-2:]
    else:
        stars_phone_number = "0049" + "***" + phone_number[-2:]
    print("...")
    time.sleep(2)
    print("Generating report...")
    time.sleep(2)
    print("...")
    print("                    -------------------------")
    print("                    | Amazon Expense Report |")
    print("                    ------------------------") 
    item_list = []
    items = {}
    items_total_cost = 0
    delivery_charges = 0
    orders_costs = []
    orders_dates = []
    today = date.today().strftime("%m/%d/%Y")
    spending_limit = 500
    for dict in purchases:
        date_ = dict["date"]
        charges_pro_item = float(dict["weight"])
        cost_pro_item = float(dict["cost"]) - float(charges_pro_item)
        total_cost = cost_pro_item * dict["quantity"]
        charges = charges_pro_item * dict["quantity"]
        items[dict["item"]] = cost_pro_item
        item_list.append(items)
        items_total_cost += total_cost
        delivery_charges += charges
        orders_costs. append(dict["cost"])
        day = datetime.strptime(date_, "%m/%d/%Y")
        orders_dates.append(day)

    most_expensive = most_expensive_item(item_list)
    least_expensive = least_expensive_item(item_list)
    average_cost = (items_total_cost+delivery_charges)/len(purchases)
    start_date = min(orders_dates).strftime("%m/%d/%Y")
    end_date = max(orders_dates).strftime("%m/%d/%Y")

    print(f"name: {name.capitalize()}       password: {password}     Tel: {stars_phone_number}     Date:{today}")
    print("------------------------------------------------")
    print(" DELIVERY CHARGES            TOTAL ITEM COST")
    print(f"    {delivery_charges:.2f} EURO", end = "                   ")                       
    print(f"{items_total_cost:.2f} EURO")
    print("")
    print("MOST EXPENSIVE               LEAST EXPENSIVE")
    print(f"name: {most_expensive[0]}", end = "                    ")                   
    print(f"name:{least_expensive[0]}")
    print(f"cost: {most_expensive[1]:.2f} EURO", end = "                  ")  
    print(f"cost:{least_expensive[1]:.2f} EURO")
    print("")
    print(f"AVERAGE COST OF ITEM PER ORDER: {average_cost:.2f} EURO")
    print(f"PURCHASE DATE RANGE: {start_date} to {end_date} ")
    print("--------")
    if sum(orders_costs) < spending_limit:
        print(f"Note: You have not exceeded the spending limit of {spending_limit} EURO")
    elif sum(orders_costs) == spending_limit:
        print(f"Note: You have reached the spending limit of {spending_limit} EURO")
    else: 
        print(f"Note: You have exceeded the spending limit of {spending_limit} EURO")
    print("")