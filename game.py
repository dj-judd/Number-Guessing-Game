import random

def menu(gameVersion, firstStart):
    gameVersionIntro = "Number Guessing Game v{}".format(gameVersion)
    menuSelection = 0

    menuText = """Menu:
1) Play Solo
2) Play vs Computer
3) Options
4) Exit"""


    while menuSelection == 0:

        if firstStart:
            firstStart = False
            print("\n" + "~" * len(gameVersionIntro) +"\n" + gameVersionIntro + "\n" + "~" * len(gameVersionIntro) +"\n")

        print(menuText)
        menuSelection = input("\nChoose an option: ")

        if inputIsValidInt(menuSelection):
            menuSelection = int(menuSelection)

            if menuSelection == 1:
                playSoloGame(rangeStart, rangeEnd, guessLimit)
            elif menuSelection == 2:
                playVsGame()
            elif menuSelection == 3:
                optionsMenu()
            elif menuSelection == 4:
                print("Exiting. Have a nice day!\n")
                exit()
            else:
                print(errorMessage)
                menuSelection = 0
        else: 
            print(errorMessage)
            menuSelection = 0

    
def optionsMenu():
    menuSelection = 0
    optionsMenuText = """Options:
1) Range
2) Guess Limit
3) Back"""

    global rangeStart
    global rangeEnd
    global guessLimit


    print(optionsMenuText)
    menuSelection = input("\nChoose an option: ")

    if inputIsValidInt(menuSelection):
        menuSelection = int(menuSelection)

        if menuSelection == 1:
            print("\nChange the Range\n")
            rangeStart = input("What would you like the start of the range to be? ")
        elif menuSelection == 2:
            playVsGame()
        elif menuSelection == 3:
            optionsMenu()
        elif menuSelection == 4:
            print("Exiting. Have a nice day!\n")
            exit()
        else:
            print(errorMessage)
            menuSelection = 0
    else: 
        print(errorMessage)
        menuSelection = 0


    
def playSoloGame(rangeStart, rangeEnd, guessLimit):

    # Random number generation
    randomNum = random.randint(rangeStart,rangeEnd)

    guessCounter = 0
    guess = 0

    username = input("Hello, what is your name? ")
    print ("Hello " + username + ", I'm thinking of a number between {} and {}.".format(rangeStart, rangeEnd))
    print ("Try to guess my number...if you dare!\n")

    # For testing
    print("\x1b[6;30;41m" + "\nThis the secret number for testing: {}\n".format(randomNum)+ "\x1b[0m")

    while guess != randomNum and guessLimit >= guessCounter:

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
                    guessCounter += 1

                elif guess < randomNum:
                    print("That is too low, try again.\n")
                    guessCounter += 1

                else:
                    print("You got it!!! And only in " + format(guessCounter) + " attempts! Amazing!!")

        # When the input is not an int.
        elif guess.lstrip("-").isdigit() and int(guess) < 0:
            print("That is a negative number bro")
        else:
            print("Silly Billy...that's not a number! Try again!\n")

def playVsGame():
    print("vs mode")


def inputIsValidInt(input):

    try:
        input = int(input)
        return True

    except ValueError:
        return False

gameVersion = 0.1
firstStart = True
errorMessage = "\x1b[6;30;41m" + "!!! Error: Not a valid option! ¡¡¡" + "\x1b[0m" + "\n"

rangeStart = 0
rangeEnd = 100

guessLimit = 0

menu(gameVersion, firstStart)