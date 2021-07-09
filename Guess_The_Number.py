import random

# guess number for user
def Guess_User(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x}:"))
        if guess > random_number :
            print("Sorry,Guess again, Your guess too high.")
        elif guess < random_number:
            print("Sorry, Guess again , Your guess too low.")
    print(f"wow,congrats. You have guessed the number {guess} correctly .")            
    
    
Guess_User(10)   
 
# guess number for computer 
def Computer_Guess(x):
    low = 1
    high= x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low    
        feedback = input(f"Is {guess} to high (H), to Low (L) .or correct (C)?").lower()
        
        if feedback == "h":
            high = guess -1
        elif feedback =="l":
            low = guess +1
    print(f"The computer guessed  your number{guess} ,correctly")            
    
Computer_Guess(10)    