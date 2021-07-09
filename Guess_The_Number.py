import random

def Guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x}:"))
        if guess > random_number :
            print("Sorry,Guess again, Your guess too high.")
        elif guess < random_number:
            print("Sorry, Guess again , Your guess too low.")
    print("wow,congrats. You have guessed the number.")            
    
    
Guess(10)    