import random

def guess_num(x):
    random_num = random.randint(1,x)
    guess_num = 0

    while (guess_num != random_num):
        guess_num = int(input(f"Guess a number between 1 to {x}: "))
        if (guess_num > random_num):
            print("Value too high, guess again!! ")

        elif (guess_num < random_num):
            print("Value too low, guess again!! ")
        
    print(f"Congrats, you've correctly guessed the random number {random_num}")

#guess_num(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(11)