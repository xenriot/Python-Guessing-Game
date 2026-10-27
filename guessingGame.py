import random

# 10 attempts to guess the number
attempts = 10

# display the rules of the game
def displayRules():
    print("Welcome to the Guessing Game!\n")
    print(f"You have {attempts} attempts to guess it.\n")
    print("After each guess, I will tell you if your guess is too high, too low, or correct.\n")
    print("Good luck!\n")
    return

# function to play the game
def playGame(number_to_guess, attempt = 1):
    # check if the user has used all attempts
    if attempt > attempts:
        print("Game Over!\n")
        print(f"You've used all your attempts! The correct number was {number_to_guess}.")
        return # exit the function if the user has used all attempts
    
    # prompt the user for their guess
    guess = input(f"Attempt {attempt}/{attempts} - enter your guess (1-100): ")
    print(f"Your guess is {guess}.\n")
    
    # check if the input is a valid integer
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input! Enter a number between 1 and 100.\n")
        playGame(number_to_guess, attempt) # ask for the guess again without incrementing the attempt
        return
    
    # check if the guess is within the valid range
    if guess < 1 or guess > 100:
        print("Invalid input! Enter a number between 1 and 100.\n")
        playGame(number_to_guess, attempt) # ask for the guess again without incrementing the attempt
        return
    
    # check if the guess is correct, too low, or too high
    check_guess = lambda x, y: "correct" if x == y else "too low" if x < y else "too high"
    result = check_guess(guess, number_to_guess)
    
    # if the guess is correct, congratulate the user and end the game
    if result == "correct":
        print("Congratulations! You've guessed the correct number.\n")
        print(f"You guessed it in {attempt} attempts!\n")
        return
    
    if result == "too low":
        print("Your guess is too low. Try again.\n")
    else:
        print("Your guess is too high. Try again.\n")
        
    playGame(number_to_guess, attempt + 1) # call the function again with incremented attempt
    
    
displayRules() # display the rules of the game again

random_number = random.randint(1, 100) # generate a new random number for the next game

playGame(random_number) # start a new game with the new random number