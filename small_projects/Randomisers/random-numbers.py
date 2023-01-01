import random

print("This small program randomises a number between 1 and the given number.\n")

def rando(x):
    rando = random.randint(1, x)
    
    if rando != 0:
        print(f"{rando}")
        again()
        

def again():
    again = input("Do you want to go again?: ")
    if again in ['Yes', 'yes', 'Y', 'y']:
        x = int(input("Number? "))
        rando(x)

    else:
        exit

def start():
    x = int(input("Number? "))
    rando(x)

start()