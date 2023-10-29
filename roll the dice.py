from random import randint
from time import sleep

def get_user_guess(): #function to get user's guess
    guess = int(input("Guess a number: ")) #prompt user to guess a number and standardizes all input as an integer
    return guess

def roll_dice(number_of_sides): #simulate rolling dice
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides*2
    print("The maximum value is ", max_val)
    guess = get_user_guess() # will return user's guess after prompting them

    if guess > max_val:
        print("Your guess is higher than the maximum possible value.")
        return
    else:
        print("Rolling...")
        sleep(2)
        print("The first roll is: ", first_roll)
        sleep(1)
        print("The second roll is: ", second_roll)
        sleep(1)
        
        total_roll = first_roll + second_roll
        print("The total value is: ", total_roll)
        print("Result...")
        sleep(1)

        if guess == total_roll:
            print("Congratulations, you won the battle against Randomness!")
        else:
            print("Why did you think you could win against Randomness?")

roll_dice(6)
