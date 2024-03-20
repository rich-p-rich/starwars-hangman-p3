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

        if guess.startswith('??') and len(guess) == 2:
            if clue1_used is True and clue2_used is False:
                attempts -= 1
                myprint("Clue 2: they mostly appear in", get_clue2(word))
                myprint("You have", attempts, "shots left \n")
                continue
            elif clue1_used is False:
                myprint("Try Clue 1 first!")
                myprint("Tap ? and enter for Clue 1.")
                clue1_used = True
                continue
            else: 
                myprint("Reminder: the answer is a", get_clue2(word))
                myprint("You have not lost any shots for this reminder.\n")