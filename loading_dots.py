
from time import sleep

def loading():
    dots = "..."
    for dot in dots:  
        print(dot, end = "", flush= True)
        sleep(0.5)
