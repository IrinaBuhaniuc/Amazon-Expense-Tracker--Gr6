import time
import sys

def login(users_register: dict):
    '''
        This function will verify if the entered username and password are correct accord to user_register dictionary.

            Parameters:
                    user_register (dict): Username as key, password as value

            Returns:
                    username (str): String of characters (letters,symbols, numbers)
                    password (str): String of characters (letters,symbols, numbers)
    '''
    print("\nPlease log in.\n")
    attempts = 0

    while attempts < 5:
        username = input("Username: ")
        password = input("Password: ")

        if username in users_register and users_register[username] == password:
            return username, password
        else:
            attempts += 1
            if attempts < 4:
                print(f"Invalid Username or password. You can try {4 - attempts} more times.")
            elif attempts == 4:
                print("You have entered 3 times incorrect username or password. Please try again after 5 seconds.")
                time.sleep(5)
            else:
                print("Please register again.")
                sys.exit()
