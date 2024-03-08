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
#print("Welcome to Starwars Hangman!")

#Homescreen
"""
Set up homescreen 
The user chooses to play the game or read the gameplay instructions 
"""
def display_homescreen():
    print('Welcome to Starwars Hangman! Save your homeworld by guessing the missing name before the Death Star is in range!\n')
    print('Choose your option:\n')
    option1 = '1. Play the game: press "1" and enter.\n'
    option2 = '2. How to play: press "2" and enter.\n'
    print(option1)
    print(option2)
    option = input("Enter your option:  ")

    if option == '1':
        print("Starting your attack run ...")
    elif option == '2':
        print("Loading up the Death Star plans now ...")
    else:
        print("No target found: please enter 1 or 2")

display_homescreen()


