'''
Name: Anannnya Abhi
Date: 14.11.24
Python program for a guessing game
'''
import random
small=int(input("Enter the small limit:"))
large=int(input("Enter the large limit:"))
random_value=random.randint(small,large)
no_of_tries=0
while True:
    guess=int(input("Enter your guess:"))
    no_of_tries=no_of_tries+1
    if guess==random_value:
        print("Congrats!You got it!")
        print(f"Number of tries={no_of_tries}")
        break
    elif guess < random_value:
        print("Too small,Try a bigger number.")
    elif guess>random_value:
        print("Too large,Try a smaller number.")