import random 

def guess(x): #defining function guess
    print("You will come up with a number and the computer will guess what it is")
    random_number = random.randint(1, x) #the random number computer will select
    guess = 0 #initializing guess at zero & guess would be wrong since it's between 1-x
    while guess != random_number: #when guess isn't the random number
        guess = int(input(f'\nGuess a number between 1 and {x}: '))
        if guess < random_number: #if guess is less than the number
            print('Sorry, guess again. Too low.')
        elif guess > random_number: #if guess is more than the number
            print('Sorry, guess again. Too high.')
    
    print(f'Yay, congrats! You have guessed the number {random_number}.')

#now we are coming up with the secret number and the computer will guess it
def computer_guess(x):
    print("The computer will come up with a number and you have to guess what it is\n")
    low = 1 #setting lowest guess computer can make
    high = x  #setting highest guess computer can make
    feedback = "" #feedback variable, initialized as an empty string
    while feedback != "c": #while feedback does not equal c (correct answer)
        if low != high: 
            computer_guess = random.randint(low, high) #guess a new random number between low and high
        else:
            computer_guess = low #could also be high because low = high
        feedback = input(f"\nIs {computer_guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h': #if we say it's too high
            high = computer_guess - 1 #the highest it can be is 1 less than computer's guess
        elif feedback == 'l': #if we say it's too low
            low = computer_guess + 1 #the lowest is 1 more than the computer's guess

    print(f"\nYay! The computer guessed your number, {computer_guess}, correctly!\n")

computer_guess(10) #makes the range from 1-10
guess(10)