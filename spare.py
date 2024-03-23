while attempts > 0:
        guess = input("Take a shot: ").lower()

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
                continue
        
        if guess.startswith('?') and len(guess) == 1:
            myprint("Clue 1: the answer is a", get_clue1(word))
            myprint("You have", attempts, "shots left \n")
            attempts -= 1
            continue

        if guess.startswith('??') and len(guess) == 2:
            myprint("Clue 2: the answer appears mostly in", get_clue2(word))
            myprint("You have", attempts, "shots left \n")
            attempts -= 1
            continue