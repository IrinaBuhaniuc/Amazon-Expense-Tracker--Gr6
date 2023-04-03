import time
import sys

def login(users_register: dict):
    print("")
    print("Please log in.")
    print("")
    time.sleep(1)
    attempts = 0 
    while attempts <5:
        username = input("Username: ")
        password = input ("Password: ")
        correct_username_password = bool

        for key in users_register:
            if username == key and password == users_register[key]:
                return username, password
            else:
                correct_username_password = False
        if not correct_username_password:
            attempts += 1
            if attempts < 4:
                print(f"Invalid Username or password. You can try {4-attempts} more times. ")
            
            elif attempts == 4:
                print("You have entered 3 times incorrect username or password. Please try again after 5 seconds.")
                time.sleep(5)
            elif attempts == 5:
                print("Please register again.")
                sys.exit()


