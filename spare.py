if guess in word:
            myprint("Great shot!")
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = guess
        else:
            attempts -= 1
            wrong_guesses.add(guess)
            myprint("Missed! Try again: you have", attempts, "shots left")
            myprint("Missed shots:", ' '.join(sorted(wrong_guesses)))

        myprint("Your target:", ' '.join(hidden_word))
        if '_' not in hidden_word:
            myprint("Great shot kid! That was one in a million:", word)
            myprint("Want to find out more?\n")
            myprint("Look it up on Wookipedia:\n")
            myprint("https://starwars.fandom.com/wiki/Main_Page\n")

        while True:    
            myprint("Choose your option:\n")
            option1 = "Play a new game: press 1 and enter"
            option2 = "Add your game to the leaderboard: press 2 and enter"
            option3 = "Return to homescreen: press 3 and enter"
            myprint(option1)
            myprint(option2)
            myprint(option3)
            option = input("   Enter your option:  ")

            if option == 1:
                myprint("Starting your attack run ... \n")
                play_the_game()
            elif option == 2:
                myprint("Get ready for your award ceremony! \n")
                leaderboard()
            elif option == 3:
                myprint("Heading back to Home One now ...")
                display_homescreen()
            else:
                myprint("No target found: please enter 1, 2 3.\n")
            break

    if attempts == 0:
        myprint("Oh no! The Death Star has won!")
        myprint("The answer was:", word)
        myprint("Don't recognise the answer?\n")
        myprint("Look it up on Wookipedia:\n")
        myprint("https://starwars.fandom.com/wiki/Main_Page\n")

        while True:    
            myprint("Choose your option:\n")
            option1 = "Play a new game: press 1 and enter"
            option2 = "View the leaderboard: press 2 and enter"
            option3 = "Return to homescreen: press 3 and enter"
            myprint(option1)
            myprint(option2)
            myprint(option2)
            option = input("   Enter your option:  ")

            if option == 1:
                myprint("Starting your attack run ... \n")
                play_the_game()
            elif option == 2:
                myprint("Get ready for your award ceremony! \n")
                leaderboard()
            elif option == 3:
                myprint("Heading back to Home One now ...")
                display_homescreen()
            else:
                myprint("No target found: please enter 1, 2 3.\n")
            break

    return attempts 

"""
Set up homescreen
The user chooses to play the game or read the gameplay instructions
"""


def clear_terminal():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Unix/Linux/MacOS
        os.system('clear')


def display_homescreen():
    myprint('Welcome to Starwars Hangman!\n')
    myprint('Save your homeworld by guessing the missing name before\n')
    myprint('the Death Star is in range!\n')

    while True:
        myprint('Choose your option:\n')
        option1 = 'Play the game: press "1" and enter.\n'
        option2 = 'How to play: press "2" and enter.\n'
        myprint(option1)
        myprint(option2)
        option = input("  Enter your option:  ")

        if option == '1':
            myprint("Starting your attack run ...\n")
            play_the_game()
        elif option == '2':
            myprint("Loading up the Death Star plans now ...\n")
            clear_terminal()
            how_to_play()
        else:
            myprint("No target found: please enter 1 or 2.\n")


display_homescreen()
