#Simple calculator

# Addition
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiply two numbers
def multiply(x, y):
    return x * y

# This function divide two numbers
def divide(x, y):
    return x / y

def uinput():
    try:
        print("Select operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        # Take input from user
        choice = int(input("Enter choice (1, 2, 3, 4): "))
        firstnumber =  int(input ("First number: "))
        secondnumber = int(input ("Second number: "))

        if choice == 1:
            print(add(firstnumber, secondnumber))
        if choice == 2:
            print(subtract(firstnumber, secondnumber))
        if choice == 3:
            print(multiply(firstnumber, secondnumber))
        if choice == 4:
            print(divide(firstnumber, secondnumber))

    except ValueError:
        print("Must use a number!")
        uinput()

uinput()