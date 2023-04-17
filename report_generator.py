from datetime import datetime, date
import time
from loading_dots import loading

def generate_report(name,phone_number, purchases):
    '''
        This function will print the report with expected information. 

            Parameters:
                    name (str): String with letters
                    phone_number (str)): Decimal string
                    purchases (list): 

            Returns:
                    it will be printed the report that contains certain information about purchases
    '''
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
    loading()
    time.sleep(1)
    print("\nGenerating report", end = "")
    loading()
    print("")
    loading()
    time.sleep(1)
    print("                    -------------------------")
    print("                    | Amazon Expense Report |")
    print("                    ------------------------") 
    all_items_name_and_cost = []
    item_name_and_cost = {}
    
    cost_per_item = 0
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
        
        item_name_and_cost[dict["item"]] = cost_pro_item
        all_items_name_and_cost.append(item_name_and_cost)
        
        cost_per_item += float(dict["cost"])
        items_total_cost += total_cost
        delivery_charges += charges
        
        orders_costs. append(dict["cost"])
        day = datetime.strptime(date_, "%m/%d/%Y")
        orders_dates.append(day)

    most_expensive = most_expensive_item(all_items_name_and_cost)
    least_expensive = least_expensive_item(all_items_name_and_cost)
    average_cost = cost_per_item/len(purchases)
    start_date = min(orders_dates).strftime("%m/%d/%Y")
    end_date = max(orders_dates).strftime("%m/%d/%Y")
    space = "                       "
    

    print(f"name: {name.capitalize()}       password: {password}     Tel: {stars_phone_number}     Date:{today}")
    print("------------------------------------------------")
    print(" DELIVERY CHARGES            TOTAL ITEM COST")
    print(f"    {delivery_charges:.2f} EURO", end = "                   ")                       
    print(f"{items_total_cost:.2f} EURO")
    print("")
    print("MOST EXPENSIVE               LEAST EXPENSIVE")
    print(f"name: {most_expensive[0]}", end = f"{space[len(most_expensive[0]):]}")                   
    print(f"name: {least_expensive[0]}")
    print(f"cost: {most_expensive[1]:.2f} EURO", end = f"{space[len(str(int(most_expensive[1])))+8:]}")  
    print(f"cost: {least_expensive[1]:.2f} EURO")
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