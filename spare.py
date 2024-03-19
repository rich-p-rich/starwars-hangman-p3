        if guess == "!":
            guess_answer = input("Guess the whole answer: ").lower()

            if guess_answer == word: 
                myprint("Great shot kid! That was one in a million:", word)
                myprint("Want to find out more? Look it up on Wookipedia: https://starwars.fandom.com/wiki/Main_Page\n')")
                input('Press enter to start a new game.\n') 
                break

            else: 
                attempts -= 1
                myprint("Missed! Try again: you have", attempts, "shots left")
                guessed_characters.add(guess)
                continue


answers_sheet = SHEET.worksheet('answers')
answers = answers_sheet.col_values(1)[1:]
clue1 = SHEET.worksheet('clue1')
clue2 = SHEET.worksheet('clue2')


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
    clue2_data = clue2.get_all_values()
    for row in clue2_data:
        if row[0] == answer:
            return row[2]