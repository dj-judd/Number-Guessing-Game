import random

def menu(gameVersion, firstStart):
    gameVersionIntro = "Guessing Game v{}".format(gameVersion)"

    if menuSelection = 0 and firstStart = True:
    # Opening Dialogue
    print("\n" + "~" * len(gameVersionIntro) +"\n" + gameVersionIntro + "\n" + "~" * len(gameVersionIntro) +"\n")


    print("""Menu:
            1) Play
            2) Options
            3) Exit""")
    
def game():
    username = input("Hello, what is your name? ")
    print ("Hello " + username + ", I'm thinking of a number between 1 and 100.")
    print ("Try to guess my number...if you dare!\n")

def userInputIsValid():

    try:
        guess = int(input("What is your guess? "))
    
    except ValueError:
        return False


    # Random number generation
    randomNum = random.randint(1,100)

gameVersion = 0.1
firstStart = True

menuSelection = 0

menu(gameVersion, firstStart)

# For testing
# print("\nThis the secret number for testing:\n" + format(randomNum) + "\n")


guess = 0
while guess != randomNum:

    userInputIsValid()

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
    elif guess.lstrip("-").isdigit() and int(guess) < 0:
        print("That is a negative number bro")
    else:
        print("Silly Billy...that's not a number! Try again!\n")



    





