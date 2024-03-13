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

def myprint(*args):
    """
    add a left margin to the statements in the Heroku terminal to make it easier to read
    """
    print(' ' ,*args)

def how_to_play():
    """
    Gameplay explanation
    """
    
    myprint('How To Play\n')
    myprint('Beat the Death Star and work out the identity of the hidden Star Wars name.\n')
    myprint('The answer can be a character, a droid, a ship, a vehicle, a type\n') 
    myprint('of trooper, a planet, a place or an alien species.\n')
    myprint('Example: _ _ _   _ _ _ _ _   _ _ _ _\n')
    myprint('You have 10 attempts: either guess one letter at a time or\n') 
    myprint('To guess the whole name, first type ! and press enter. Then enter your guess.\n')
    myprint('guess the whole name.\n')
    myprint('If you guess a letter and it is right, the letter will appear wherever\n') 
    myprint('it appears.\n')
    myprint('_ _ E   _ E _ _ _   _ _ _ _\n')
    myprint('If your guess is wrong, the game will simply continue depending on\n') 
    myprint('how many attempts you have left.\n')
    myprint('If you get stuck, you can ask for up to two clues. Each clue will\n') 
    myprint('use up one attempt.\n')
    myprint('Type ? and hit enter for Clue One.\n') 
    myprint('Clue One will tell you whether the name is a character, a ship, and so on.\n')
    myprint('Type ?? and hit enter for Clue Two.\n')
    myprint('Clue Two will tell you what set of films and / or TV series\n') 
    myprint('they are seen most in.\n')
    myprint('_ _ E   _ E _ _ _   _ _ _ _\n')
    myprint('Clue one: a place.\n')
    myprint('_ H E   _ E _ _ H   _ _ _ R\n')
    myprint('Clue two: the Original Trilogy.\n')
    myprint('T H E   D E A T H   S T A R \n')
    input('Press enter to play the game:  \n')
    ("Starting your attack run ...\n")
    play_the_game()



#Gameplay section 

def import_word(answers):
    """
    Import random word from the answers sheet
    """
    word = random.choice(answers).lower().strip()
    return word

def clue(): 
    """
    Function for giving the players clue 1 or clue 2
    """
    

def play_the_game():
    """
    Function for playing the game
    """
    word = import_word(answers).lower().strip()
    hidden_word = ['_' if letter != ' ' else ' ' for letter in word]
    guessed_characters = set() #keeps track of all guesses in case user repeats a guess 
    wrong_guesses = set() #keeps track of wrong guesses to display them to the user

    if len(word) <= 10:  #Sets the conditions for the number of wrong guesses the user is allowed based on the length of the word
        attempts = 6
    else:   
        attempts = 10

    myprint("Your target:", ' '.join(hidden_word))
    myprint('\n')
    myprint("You have",attempts,"shots to save your planet.")
    myprint('\n')

    while attempts > 0:
        guess = input("Take a shot! Guess a letter: ").lower()

        if len(guess) != 1:  #the player should only enter 1 character at a time unless they want to guess the whole thing
            myprint("Only one character at a time! Or press ! and then 'enter' to guess the whole answer")
            continue
        
        if guess in guessed_characters:
            myprint("You've taken that shot already - try something else!")
            continue

        guessed_characters.add(guess)
                
        if guess in word:
            myprint("Great shot!")
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = guess
        else:
            attempts -= 1 
            wrong_guesses.add(guess)
            myprint("Just missed! Try again: you have", attempts, "shots left")
            myprint("Missed shots:", ' '.join(sorted(wrong_guesses))) #displays wrong guesses
            
        myprint("Your target:", ' '.join(hidden_word))
        if '_' not in hidden_word:
            myprint("Great shot kid! That was one in a million:", word)
            myprint("Don't recognise the answer? Look it up on Wookipedia: https://starwars.fandom.com/wiki/Main_Page')")
            input('Press enter to start a new game:  \n')
            ("Starting your attack run ...\n")
            play_the_game()
            break

    if attempts == 0:
        myprint("Oh no! The Death Star has won!")
        myprint("The answer was:", word)
        myprint("Don't recognise the answer? Look it up on Wookipedia: https://starwars.fandom.com/wiki/Main_Page')")
    input('Press enter to play the game:  \n')
    ("Starting your attack run ...\n")
    play_the_game()


#Homescreen
"""
Set up homescreen 
The user chooses to play the game or read the gameplay instructions 
"""
def display_homescreen():
    myprint('Welcome to Starwars Hangman!\n')
    myprint('Save your homeworld by guessing the missing name before\n') 
    myprint('the Death Star is in range!\n')
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
        how_to_play() 
    else:
        myprint("No target found: please enter 1 or 2.\n")

display_homescreen()

