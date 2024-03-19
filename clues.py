    word = import_word(answers).lower().strip()
    hidden_word = [letter if letter in (" ", "'", "-") else '_' for letter in word]
    guessed_characters = set() #keeps track of all guesses in case user repeats a guess
    wrong_guesses = set() #keeps track of wrong guesses to display them to the user
    invalid_characters = [' ', '#', '*', '<', '>', ':', ';', '(', ')', '+', '-', 'ü', 'ö', 'ä', 'ß', '/', '%', '{', '}']
    clue1_used = False # default setting: only turns true after clue1 is used -> stops user from using clue2 before clue 1
    clue1_reminders = 0
    clue2_used = False # default setting
    clue2_reminders = 0

    if len(guess) == 1 and guess not in invalid_characters and guess not in guessed_characters:
            if guess.startswith('!'):
                guess = input("Guess the whole answer: ").lower()
                if guess == word:
                    myprint("Great shot kid! That was one in a million:", word)
                    myprint("Want to find out more? Look it up on Wookieepedia: https://starwars.fandom.com/wiki/Main_Page")
                    input('Press enter to start a new game:  \n')
                    ("Starting your attack run ...\n")
                    play_the_game()
                    break
                else:
                    attempts -= 1
                    myprint("Missed! Try again: you have", attempts, "shots left \n")
                    
            if guess.startswith('?') and len(guess) == 1 and clue1_used == False:
                attempts -= 1
                myprint("Clue 1: the answer is a", get_clue1(word))
                myprint("You have", attempts, "shots left \n")
                clue1_used = True
                continue
            
            else:
                if clue1_used == True:
                    myprint("Reminder (no further attempts lost):")
                    myprint("Clue 1: the answer is a", get_clue1(word))
                continue
                
            if guess.startswith('??') and len(guess) == 2:
                if clue1_used == True:
                    attempts -= 1
                    myprint("Clue 2: the answer appears mostly in", get_clue2(word))
                    myprint("You have", attempts, "shots left \n")
                 
                elif clue1_used == False:
                    myprint("Try Clue 1 first!")
                    myprint("Tap ? and enter for Clue 1.")
                  
                else:
                    if clue2_used == True:
                        myprint("Reminder (no further attempts lost):")
                        myprint("Clue 2: the answer is a", get_clue2(word))
                 
