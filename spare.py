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