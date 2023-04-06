import re
import sys
import os
import time 


def password_validator(password: str)->bool:
    '''
        This function will verify if the password is valid according to requirements.
            Requirements:
            - Should have at least one number.
            - Should have at least one uppercase and one lowercase character.
            - Should have at least one special symbol.
            -Should be between 6 to 20 characters long.
            -If the password is not valid the user will be ask to try again with a valid password, then exit the program.
            
            Parameters:
                    password (str): String of characters (letters,symbols, numbers)

            Returns:
                    True or False, in case if password is valid or not.
    '''   
    upper = bool(re.search("[A-Z]", password))
    lower = bool(re.search("[a-z]", password)) 
    numeric = bool(re.search("[0-9]", password))
    symbol = bool

    for char in password:
        if char.isalnum():
            symbol = False
        else:
            symbol = True
            break
    if len(password) >=6 and len(password) <=20 and upper== True and lower==True and numeric==True and symbol==True:
        return True
    else:
        print("Password is not valid")
        if len(password) <6 or len(password) >20:
            print("Your password should be between 6 to 20 characters long.")
        if upper== False or lower == False:
            print("Your password should have at least one uppercase and one lowercase character.")
        if numeric == False:
            print("Your password should have at least one number.")
        if symbol == False:
            print("Your password should have at least one special symbol.")
        print("Pleas try again with a valid password.\n")
        time.sleep(2)
        print("Quitting program...")
        time.sleep(3)
        sys.exit()
            
        
        
