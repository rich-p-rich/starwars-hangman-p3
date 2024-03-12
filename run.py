import gspread
import random
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

answers_sheet = SHEET.worksheet('answers')
answers = answers_sheet.col_values(1)[1:] 
clue1 = SHEET.worksheet('clue1')
clue2 = SHEET.worksheet('clue2')

#data = answers.get_all_values()
#print(data)
#print("Welcome to Starwars Hangman!")

def how_to_play():
    """
    Gameplay explanation
    """
    
    print()
    print('How To Play\n')
    print('Beat the Death Star and work out the identity of the hidden Star Wars name.\n')
    print('The answer can be a character, a droid, a ship, a vehicle, a type of trooper, a planet, a place or an alien species.\n')
    print('Example: _ _ _   _ _ _ _ _   _ _ _ _\n')
    print('You have 10 attempts: either guess one letter at a time or guess the whole name.\n')
    print('If you guess a letter and it is right, the letter will appear wherever it appears.\n')
    print('_ _ E   _ E _ _ _   _ _ _ _\n')
    print('If your guess is wrong, the game will simply continue depending on how many attempts you have left.\n')
    print('If you get stuck, you can ask for up to two clues. Each clue will use up one attempt.\n')
    print('Clue one will tell you whether the name is a character, a ship, and so on.\n')
    print('Clue two will tell you what set of films and / or TV series they are seen most in.\n')
    print('_ _ E   _ E _ _ _   _ _ _ _\n')
    print('Clue one: a place.\n')
    print('_ H E   _ E _ _ H   _ _ _ R\n')
    print('Clue two: the Original Trilogy.\n')
    print('T H E   D E A T H   S T A R \n')
    input('Press 1 and enter to play the game:  \n')
    ("Starting your attack run ...\n")
    play_the_game()



#Gameplay section 

def import_word(answers):
    """
    Import random word from the answers sheet
    """
    word = random.choice(answers).lower().strip()
    return word

def play_the_game():
    """
    Function for playing the game
    """
    word = import_word(answers).lower().strip()
    hidden_word = ['_' if letter != ' ' else ' ' for letter in word]
    guessed_letters = set()
    attempts = 10

    print("Your target:", ' '.join(hidden_word))

    while attempts > 0:
        guess = input("Take a shot! Guess a letter: ")
        if guess in word:
            print("Great shot!")
        else:
            print("Just missed! Try again")
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
        print("Your target:", ' '.join(hidden_word))
        if '_' not in hidden_word:
            print("Great shot kid! That was one in a million:", word)
            print("Don't recognise the answer? Look it up on Wookipedia: https://starwars.fandom.com/wiki/Main_Page')")
            input('Press 1 and enter to start a new game:  \n')
            ("Starting your attack run ...\n")
            play_the_game()
            break

#Homescreen
"""
Set up homescreen 
The user chooses to play the game or read the gameplay instructions 
"""
def display_homescreen():
    print('Welcome to Starwars Hangman!')
    print('Save your homeworld by guessing the missing name before the Death Star is in range!\n')
    print('Choose your option:\n')
    option1 = 'Play the game: press "1" and enter.\n'
    option2 = 'How to play: press "2" and enter.\n'
    print(option1)
    print(option2)
    option = input("Enter your option:  ")

    if option == '1':
        print("Starting your attack run ...\n")
        play_the_game()
    elif option == '2':
        print("Loading up the Death Star plans now ...\n")
        how_to_play() 
    else:
        print("No target found: please enter 1 or 2.\n")

display_homescreen()

