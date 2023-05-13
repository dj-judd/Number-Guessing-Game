"""A number-guessing game."""
import random

# Random number generation
randomNum = random.randint(1,100)

tryCounter = 0

# For testing
# print("\nThis the secret number for testing:\n" + format(randomNum) + "\n")

# Opening Dialogue 
username = input("Hello, what is your name? ")
print ("Hello " + username + ", I'm thinking of a number between 1 and 100.")
print ("Try to guess my number...if you dare!\n")

guess = 0
while guess != randomNum:

    guess = input("What is your guess? ")

    # Input sanitation
    # Is it an int?
    if guess.isdigit():

        guess = int(guess)

        # If so, is it in range?
        if guess < 1 or guess > 100:
            print("That's out of bounds. Remember between 1 & 100.\n")

        else:
            if guess > randomNum:
                print("That is too high, try again.\n")
                tryCounter += 1

            elif guess < randomNum:
                print("That is too low, try again.\n")
                tryCounter += 1

            else:
                print("You got it!!! And only in " + format(tryCounter) + " attempts! Amazing!!")

    # When the input is not an int.
    else:
        print("Silly Billy...that's not a number!\nOr it's a negative...either way, try again!\n")