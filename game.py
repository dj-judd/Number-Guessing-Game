import random
import sys

def menu(gameVersion, debugMode, firstStart, defaultRange, defaultGuessLimit):
    gameVersionIntro = "Number Guessing Game v{}".format(gameVersion)
    menuSelection = 0

    rangeStart = defaultRange[0]
    rangeEnd = defaultRange[1]
    guessLimit = defaultGuessLimit

    menuText = """Main Menu:
1) Play Solo
2) Play vs Computer
3) Options
5) Exit"""


    while menuSelection == 0:

        if firstStart:
            firstStart = False
            print("\n" + "~" * len(gameVersionIntro) +"\n" + gameVersionIntro + "\n" + "~" * len(gameVersionIntro))

        print("\n" + menuText)
        menuSelection = input("\nChoose an option: ")

        if inputIsValidInt(menuSelection):
            menuSelection = int(menuSelection)

            if menuSelection == 1:
                menuSelection = 0
                playSoloGame(rangeStart, rangeEnd, guessLimit, debugMode)
            elif menuSelection == 2:
                menuSelection = 0
                playVsCompGame(rangeStart, rangeEnd, guessLimit, debugMode)
            elif menuSelection == 3:
                menuSelection = 0
                rangeStart, rangeEnd, guessLimit = optionsMenu(defaultRange, defaultGuessLimit)
            elif menuSelection == 5:
                print("Exiting. Have a nice day!\n")
                break
            else:
                print("\n" + getNotValidErrorMessage())
                menuSelection = 0
        else: 
            print("\n" + getNotValidErrorMessage())
            menuSelection = 0

    
def optionsMenu(defaultRange, defaultGuessLimit):
    rangeStart = defaultRange[0]
    rangeEnd = defaultRange[1]
    guessLimit = defaultGuessLimit

    menuSelection = 0


    while menuSelection == 0:

        optionsMenuText = """Options:
1) Change Range ({}~{})
2) Change Guess Limit ({})
5) Back""".format(rangeStart, rangeEnd, guessLimit)

        print("\n" + optionsMenuText)
        menuSelection = input("\nChoose an option: ")

        if inputIsValidInt(menuSelection):
            menuSelection = int(menuSelection)

            if menuSelection == 1:
                print("\nChange the Range")
                rangeStart = input("What would you like the start of the range to be? ")

                if inputIsValidInt(rangeStart):
                    rangeStart = int(rangeStart)

                rangeEnd = input("What would you like the end of the range to be? ")

                if inputIsValidInt(rangeEnd):
                    rangeEnd = int(rangeEnd)

                    if rangeStart >= rangeEnd:
                        print("\n" + getNotValidErrorMessage())
                        print("The start of the range can't be less than the end. Reseting to Defaults")
                        rangeStart == defaultRange[0]
                        rangeEnd == defaultRange[1]
                        menuSelection = 0
                    menuSelection = 0

            elif menuSelection == 2:
                guessLimit = input("\nWhat do you want the new Guess Limit to be? ")

                if inputIsValidInt(guessLimit):
                    guessLimit = int(guessLimit)

                    if guessLimit <= 0:
                        print("...I don't think you can guess negative times...")
                        guessLimit = 0
                        menuSelection = 0
                        
                    else:
                        print("\nYou got it! New Guess Limit is \033[1m{}\033[0m".format(guessLimit))
                        menuSelection = 0
                else:
                    print(getNotValidErrorMessage())
                    menuSelection = 0

            elif menuSelection == 5:
                return rangeStart, rangeEnd, guessLimit

            else:
                print(getNotValidErrorMessage())
                menuSelection = 0
        else: 
            print(getNotValidErrorMessage())
            menuSelection = 0
    
    return rangeStart, rangeEnd, guessLimit


    
def playSoloGame(rangeStart, rangeEnd, guessLimit, debugMode):
    replayed = False

    while True:

        # Random number generation
        randomNum = random.randint(rangeStart,rangeEnd)

        guessCounter = 1
        guess = 0

        if not replayed:
            username = input("Hello, what is your name? ")
        print ("Hello " + username + ", I'm thinking of a number between {} and {}.".format(rangeStart, rangeEnd))
        print ("Try to guess my number...if you dare! I'll give you {} tries.\n".format(guessLimit))

        # For testing
        if debugMode:
            print("\x1b[6;30;41m" + "This the secret number for testing: {}".format(randomNum)+ "\x1b[0m\n")

        while guess != randomNum and guessLimit >= guessCounter:

            guess = input("What is your guess? ")

            if inputIsValidInt(guess):
                guess = int(guess)

                if guess < rangeStart or guess > rangeEnd:
                    print("That's out of bounds. Remember between {} & {}.\n".format(rangeStart, rangeEnd))
                    guessCounter += 1

                else:
                    if guess > randomNum:
                        print("That is too high, try again.\n")
                        guessCounter += 1

                    elif guess < randomNum:
                        print("That is too low, try again.\n")
                        guessCounter += 1

                    else:
                        print("\nYou got it!!! And only in {} attempts! Amazing!!\n".format(guessCounter))
                        guessCounter += 1
            else:
                print(getNotValidErrorMessage())
        
        replayed = True

        if not replay():
            break


def playVsCompGame(rangeStart, rangeEnd, guessLimit, debugMode):
    replayed = False

    while True:

        # Random number generation
        trueRandomNum = random.randint(rangeStart,rangeEnd)
        opponentsRandomNum = random.randint(rangeStart,rangeEnd)

        guessCounter = 1
        guess = 0

        if not replayed:
            username = input("Hello, I'm a computer and I'll be your opponent today. What is your name? ")
        print ("Okay " + username + ", I'm thinking of a number between {} and {}.".format(rangeStart, rangeEnd))
        print ("Try to guess my number. And then I'll try. You'll have {} tries.\n".format(guessLimit))

        # For testing
        if debugMode:
            print("\x1b[6;30;41m" + "\nThis the secret number for testing: {}".format(trueRandomNum)+ "\x1b[0m\n")

        while guess != trueRandomNum and guessLimit >= guessCounter:

            guess = input("What is your guess? ")

            if inputIsValidInt(guess):
                guess = int(guess)

                if guess < rangeStart or guess > rangeEnd:
                    print("That's out of bounds. Remember between {} & {}.\n".format(rangeStart, rangeEnd))
                    guessCounter += 1

                else:
                    if guess > trueRandomNum:
                        print("That is too high, try again.\n")
                        guessCounter += 1

                    elif guess < trueRandomNum:
                        print("That is too low, try again.\n")
                        guessCounter += 1

                    else:
                        print("\nYou got it!!! And only in {} attempts! Amazing!!\n".format(guessCounter))
                        guessCounter += 1
            else:
                print(getNotValidErrorMessage())
        
        replayed = True

        if not replay():
            break


def inputIsValidInt(input):

    try:
        input = int(input)
        return True

    except ValueError:
        return False
    

def replay():
    while True:
        replayResponse = input("Play again? (Y/n) ").lower().strip()
        if replayResponse in ["", "y", "yes"]:  # Added "" for the case when user just hits enter
            print("\n" + "~" * 50 + "\n\n\n")
            return True
        elif replayResponse in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def handle_arguments():
    debugMode = False
    otherOptions = []

    for arg in sys.argv[1:]:
        if arg == "--debug" or arg == "--d":
            debugMode = True
            if arg == "--d":
                arg = "--debug"
            otherOptions.append(arg)
        # Add more elif conditions here for other arguments.
        else:
            otherOptions.append(arg)

    return debugMode, otherOptions

def getNotValidErrorMessage():
    return "\x1b[6;30;41m" + "!!! Error: Not a valid option! ¡¡¡" + "\x1b[0m"

def main():
    gameVersion = 0.4
    firstStart = True

    defaultRange = [0, 100]

    defaultGuessLimit = 9999

    debugMode, options = handle_arguments()

    if debugMode:
        print("Debug Mode -- ON")
        print("\x1b[33;49mOptions turned on: \x1b[0m", end = " ")
        for option in options:
            print("\x1b[35;49m" + option + "\x1b[0m", end = " ")
        print()

    menu(gameVersion, debugMode, firstStart, defaultRange, defaultGuessLimit)

if __name__ == "__main__":
    main()