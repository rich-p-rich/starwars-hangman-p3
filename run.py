import gspread
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

answers = SHEET.worksheet('answers')

data = answers.get_all_values()

#print(data)

print("Welcome to Starwars Hangman!")

#How to play

def gameplay():
    '''
    Gameplay explanation
    '''
    
    print()
    print('How To Play')
    print('Beat the Death Star and work out the identity of the hidden Star Wars name.\n')
    print('The answer can be a character, a droid, a ship, a vehicle, a planet, a place or an alien species.\n')
    print('_ _ _   _ _ _ _ _   _ _ _ _\n')
    print('You have 10 attempts: either guess one letter at a time or guess the whole name.\n')
    print('If you guess a letter and it is right, the letter will appear wherever it appears in the word.\n')
    print('_ _ E   _ E _ _ _   _ _ _ _\n')
    print('If your guess is wrong, the game will simpley continue depending on how many attempts you have left.\n')
    print('If you get stuck, you can ask for up to two clues. Each clue will use up one attempt.\n')
    print('Clue one will tell you whether the name is a character, a ship, etc, clue 2 will tell you what set of films and / or TV series they are seen most in.\n')
    print('Clue one: a place.\n')
    print('Clue two: the Original Trilogy.\n')
    print('T H E   D E A T H   S T A R \n')



    return gameplay