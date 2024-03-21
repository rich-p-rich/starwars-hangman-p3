import gspread
import random
import os
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('starwars_hangman')

sw_hangman_answers = SHEET.worksheet('answers')
answers = sw_hangman_answers.col_values(1)[1:]
clue1 = sw_hangman_answers.col_values(2)[1:]
clue2 = sw_hangman_answers.col_values(3)[1:]
sw_hangman_leaderboard = SHEET.worksheet('leaderboard')


def myprint(*args):
    """
    add a left margin to the statements in the Heroku terminal
    to make it easier to read
    """
    myprint = print(' ', *args)


def how_to_play():
    """
    Gameplay explanation
    """

    myprint('How To Play\n')
    myprint('The answer can be a character, droid, ship, vehicle,\n')
    myprint('type of trooper, creature, planet, place or an alien species.\n')
    myprint('Example: _ _ _   _ _ _ _ _   _ _ _ _\n')
    myprint('You have 10 attempts: either guess one letter at a time or\n')
    myprint('If your guess is right, the letter appears as appropriate\n')
    myprint('_ _ E   _ E _ _ _   _ _ _ _\n')
    myprint('If your guess is wrong, the game continues depending on\n')
    myprint('how many attempts you have left.\n')
    myprint('You can ask for up to two clues. Each clue will\n')
    myprint('use up one attempt.\n')
    myprint('Type ? and hit enter for Clue One.\n')
    myprint('Clue 1 tells you what the target is, eg a character or a ship.\n')
    myprint('Type ?? and hit enter for Clue Two.\n')
    myprint('Clue Two will tell you what set of films and / or TV series\n')
    myprint('they are seen most in.\n')
    myprint('_ _ E   _ E _ _ _   _ _ _ _\n')
    myprint('Clue one: a place.\n')
    myprint('_ H E   _ E _ _ H   _ _ _ R\n')
    myprint('Clue two: the Original Trilogy.\n')
    myprint('To guess the whole name: type ! and press enter.\n')
    myprint('Then enter your guess.\n')
    myprint('guess the whole name.\n')
    myprint('T H E   D E A T H   S T A R \n')
    input('Press enter to play the game:  \n')
    ("Starting your attack run ...\n")
    play_the_game()


"""
Gameplay section
"""


def import_word(answers):
    """
    Import random word from the answers sheet: converts letters
    to lower case, removes trailing blanks that may exist in the 
    source google spreadsheet
    """
    word = random.choice(answers).lower().strip() 
    return word # this is the target to be guessed


def get_clue1(answer):
    """
    Function for giving the players clue 1
    """
    clue1_data = sw_hangman_answers.get_all_values()
    for row in clue1_data:
        word = row[0].lower().strip()
        if word == answer:
            return row[1]


def get_clue2(answer):
    """
    Function for giving the players clue 2
    """
    clue2_data = sw_hangman_answers.get_all_values()
    for row in clue2_data:
        word = row[0].lower().strip()
        if word == answer:
            return row[2]


def play_the_game():

    """
    Function for playing the game
    """
    word = import_word(answers).lower().strip()
    hidden_word = [letter if letter in (" ", "'", "-")
                   else '_' for letter in word]
    guessed_characters = set()  # monitors guesses in case user repeats a guess
    wrong_guesses = set()  # monitors wrong guesses to display them to the user
    invalid_characters = [' ', '#', '*', '<', '>', ':', ';', '(', ')', '+',
                          '-', 'ü', 'ö', 'ä', 'ß', '/', '%', '{', '}'] 
    clue1_used = False  # this tracks whether clue1 has been used or not
    clue2_used = False  # this tracks whether clue2 has been used or not 

    """
    This sets the nr of wrong guesses the user is allowed.
    This is based on total nr of characters in the target and can be changed here
    if required.
    """
    if len(word) <= 6:
        attempts = 6
    else:
        attempts = 10

    attempts_used = len(word) - attempts # calculate nr of attempts used
    total_guesses = 0

    myprint("Your target:", ' '.join(hidden_word))
    myprint('\n')
    myprint("You have", attempts, "shots to save your planet.")
    myprint('\n')

    while attempts > 0:
        guess = input("Take a shot: ").lower()

        """
        Invalid characters (empty input with the
        return key is handled with the 1 character only
        validation condition below)
        """
        if guess.startswith(tuple(invalid_characters)):
            myprint("Invalid input! Stay on target!")
            continue

        total_guesses += 1

        """
        Conditions for guessing the whole answer using the ! 
        """
        if guess.startswith('!'):
            guess = input("Guess the whole answer: ").lower()
            if guess == word:
                myprint("Great shot kid! That was one in a million:", word) # player wins with a guess
                myprint("Want to find out more?\n")
                myprint("Look it up on Wookieepedia:\n")
                myprint("https://starwars.fandom.com/wiki/Main_Page\n")
                myprint("Choose your option:\n")
                option1 = "Play a new game: press 1 and enter"
                option2 = "Add your game to the leaderboard: press 2 and enter"
                option3 = "Return to homescreen: press 3 and enter"
                myprint(option1)
                myprint(option2)
                myprint(option3)
                option = input("   Enter your option:  ")

                if option == '1':
                    myprint("Starting your attack run ... \n")
                    play_the_game()
                    return
                elif option == '2':
                    myprint("Get ready for your award ceremony! \n")
                    name = input("Enter your name: ")  
                    update_leaderboard(name, word, attempts)
                    leaderboard_page()
                    return
                elif option == '3':
                    myprint("Heading back to Home One now ...")
                    display_homescreen()
                    return
                else:
                    myprint("No target found: please enter 1, 2, or 3.\n")
                break
            else:
                attempts -= 1
                myprint(f"Missed! Try again: {attempts_used} out of {len(word)} attempts used") # player's guess whole answer was wrong
                continue

        """
        Conditions for asking for clues 1 and 2
        """
        if guess.startswith('?') and len(guess) == 1:
            if clue1_used is False and clue2_used is False:
                attempts -= 1
                myprint("Clue 1: the answer is a", get_clue1(word))
                myprint("You have", attempts, "shots left \n")
                clue1_used = True
            else:
                myprint("Reminder: the answer is a", get_clue1(word))
                myprint("You have not lost any shots for this reminder.\n")
            continue

        elif guess.startswith('??') and len(guess) == 2:
            if clue1_used is True and clue2_used is False:
                attempts -= 1
                myprint("Clue 2: they mostly appear in", get_clue2(word))
                myprint("You have", attempts, "shots left \n")
                clue2_used = True
            elif clue1_used is False:
                myprint("Try Clue 1 first!")
                myprint("Tap ? and enter for Clue 1.")
            else:
                myprint("Reminder: the answer is a", get_clue2(word))
                myprint("You have not lost any shots for this reminder.\n")
            continue

        """
        Ensure the user enters only 1 charaacter
        except for ?? and whole answer guesses
        """
        if len(guess) != 1:  # this makes hitting the return key on its own an invalid input
            myprint("Invalid input! Enter a single character\n")
            myprint("or enter an ! and guess the whole answer.\n")
            continue

        """
        Checks if the user is repeating a guess
        and reminds them if they are; modifies the variable
        guessed_characters (declared in the play_the_game function at line 116)
        """
        if guess in guessed_characters:
            myprint("You've taken that shot already - try something else!")
            continue

        guessed_characters.add(guess)
        

        """
        Checks guess against answer, react accordingly
        Stores wrong guesses and displays them to player
        """
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
            myprint("Great shot kid! That was one in a million:", word)  # player wins
            myprint("Want to find out more?\n")
            myprint("Look it up on Wookipedia:\n")
            myprint("https://starwars.fandom.com/wiki/Main_Page\n")
            myprint("Choose your option:\n")
            option1 = "Play a new game: press 1 and enter"
            option2 = "Add your game to the leaderboard: press 2 and enter"
            option3 = "Return to homescreen: press 3 and enter"
            myprint(option1)
            myprint(option2)
            myprint(option3)
            option = input("   Enter your option:  ")

            if option == '1':
                myprint("Starting your attack run ... \n")
                play_the_game()
                return
            elif option == '2':
                myprint("Get ready for your award ceremony! \n")
                name = input("Enter your name: ")
                update_leaderboard(name, word, attempts)
                leaderboard_page()
                return
            elif option == '3':
                myprint("Heading back to Home One now ...")
                display_homescreen()
                return
            else:
                myprint("No target found: please enter 1, 2, or 3.\n")
            break
            

    if attempts == 0:
        myprint("Oh no! The Death Star has won!")  # player loses
        myprint("The answer was:", word)
        myprint("Don't recognise the answer?\n")
        myprint("Look it up on Wookipedia:\n")
        myprint("https://starwars.fandom.com/wiki/Main_Page\n")
        myprint("Choose your option:\n")
        option1 = "Play a new game: press 1 and enter"
        option2 = "Add your game to the leaderboard: press 2 and enter"
        option3 = "Return to homescreen: press 3 and enter"
        myprint("Choose your option:\n")
        option1 = "Play a new game: press 1 and enter"
        option2 = "View the leaderboard: press 2 and enter"
        option3 = "Return to homescreen: press 3 and enter"
        myprint(option1)
        myprint(option2)
        myprint(option3)
        option = input("   Enter your option:  ")

        if option == '1':
            myprint("Starting your attack run ... \n")
            play_the_game()
            return
        elif option == '2':
            myprint("Going the the award ceremony. No medal for you, Chewie!\n")
            leaderboard_page()
            return
        elif option == '3':
            myprint("Heading back to Home One now ...")
            display_homescreen()
            return
        else:
            myprint("No target found: please enter 1, 2, or 3.\n")

            
def leaderboard_page():
    """
    Display the leaderboard and prompt the player to input their name
    """
    
    leaderboard_sheet = SHEET.worksheet('leaderboard')
    leaderboard_data = leaderboard_sheet.get_all_records()
    myprint("Leaderboard:")
    for entry in leaderboard_data:
        myprint(f"Player: {entry['Name']}, Guessed Word: {entry['Guessed Word']}, Number of Guesses: {entry['Number of Guesses']}")
    

def clear_terminal():
    """
    Set up homescreen
    The user chooses to play the game or read the gameplay instructions
    """
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
        option1 = 'Play the game: press 1 and enter.\n'
        option2 = 'View the leaderboard: press 2 and enter\n'
        option3 = 'How to play: press 3 and enter.\n'
        myprint(option1)
        myprint(option2)
        myprint(option3)
        option = input("  Enter your option:  ")

        if option == '1':
            myprint("Starting your attack run ...\n")
            play_the_game()
        elif option == '2':
            myprint("Leaderboard loading ...\n")
            leaderboard_page()            
        elif option == '3':
            myprint("Loading up the Death Star plans now ...\n")
            clear_terminal()
            how_to_play()
        else:
            myprint("No target found: please enter 1 or 2.\n")


def leaderboard():
    """
    Function to update and display the leaderboard
    """
    leaderboard_sheet = SHEET.worksheet('leaderboard')
    leaderboard_data = leaderboard_sheet.get_all_records()
    myprint("Leaderboard:")
    for entry in leaderboard_data:
        myprint(f"Player: {entry['Name']}, Guessed Word: {entry['Guessed Word']}, Attempts: {entry['Attempts']}")
    
def update_leaderboard(name, word, attempts):
    """
    Function to update the leaderboard with the player's information
    """
    leaderboard_sheet = SHEET.worksheet('leaderboard')
    leaderboard_sheet.append_row([name, word, attempts])

display_homescreen()