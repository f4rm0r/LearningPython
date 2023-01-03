import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    try:
        while guess != random_number:
            guess = int(input (f"Guess a number between 1 and {x}: "))

            if guess < random_number:
                print("your guess was too low.")

            elif guess > random_number:
                print("Your guess was too high.")
        
            elif guess == random_number:
                print (f"You guessed correct number! number was {random_number}")
                again()
        
            continue
        
    except ValueError:
        print("must guess a number! Exiting.")
        exit
    
    except NameError:
        quit

    


def again():
    again = str(input("Do you want to play again? "))
    
    if again in ['y', 'yes', 'Yes', 'Y']:
        start()
    
    else:
        exit



def start():
    diff = str(input("Easy, Medium or Hard difficulty? "))

    if diff in ['easy', 'E', 'e', 'Easy', 'ea', 'Ea', 'ease', 'Ease']:
        x = 50
        guess(x)
    

    if diff in ['m', 'M','Medium', 'medium', 'med', 'Med']:
        x = 1000
        guess(x)

    if diff in ['Hard', 'hard', 'h', 'H', 'Ha', 'ha']:
        x = 100000
        guess(x) 
    
    else:
        exit

start()