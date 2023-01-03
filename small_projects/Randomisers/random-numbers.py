import random
import sys

print("This small program randomises a number between 1 and the given number.\n")

def rando(x):
    rando = random.randint(1, x)
    
    if rando != 0:
        print(f"{rando}")
        again()
        

def again():
    try:
        again = input("Do you want to go again?: ")
        if again in ['Yes', 'yes', 'Y', 'y']:
            x = int(input("Number? "))
            rando(x)

    except ValueError:
        print("Need to be a number! Exiting.")
        sys.exit

def start():
    try:
        x = int(input("Number? "))
        rando(x)
        
    except ValueError:
        print("Need to be a number! Exiting.")
        sys.exit

start()