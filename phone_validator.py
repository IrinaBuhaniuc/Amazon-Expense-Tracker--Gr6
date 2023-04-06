import re

def phoneNumberValidator() -> str:
    '''
        Returns the a valid german mobil number.

            Parameters:
                    no parameters

            Returns:
                    phone_number (str): String of numbers and character
    '''
    while True:
        phone_number = input("Enter your phone number (ex. +49**********): ")
        if re.match(r"((\+49)|(0049))1(([5-7][0-9])|(9[0-9]))[0-9]{7,10}", phone_number):
            return phone_number
        print("Please enter a valid German phone number (ex. +49************)")
