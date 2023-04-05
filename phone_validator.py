import re

def phoneNumberValidator() -> str:
    while True:
        phone_number = input("Enter your phone number (ex. +49************): ")
        if re.match(r"((\+49)|(0|0049))1(([5-7][0-9])|(9[0-9]))[0-9]{7,10}", phone_number):
            return phone_number
            break
        print("Please enter a valid German phone number (ex. +49************)")

print(phoneNumberValidator()) 