
def play_the_game():
    """
    Function for playing the game
    """
    word = import_word(answers).lower().strip()
    hidden_word = ['_' if letter != ' ' else ' ' for letter in word]
    guessed_characters = set()
    if len(word) <= 10:
        attempts = 6
    else:   
        attempts = 10

    myprint("Your target:", ' '.join(hidden_word))
    myprint('\n')
    myprint("You have",attempts,"shots to save your planet.")
    myprint('\n')
    
    while attempts > 0:
        guess = input("Take a shot! Guess a letter: ")
        guessed_characters.add(guess)
        if guess in word:
           myprint("Great shot!")
        elif guess in guessed_characters:
            myprint("You've already used that shot. Try a different one!")
        else:
            attempts -= 1 
            myprint("You missed! Try again: you have", attempts, "shots left")
            guessed_characters.add(guess)
            if attempts == 0:
                break
           
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
        myprint("You have so far tried:", ' '.join(guessed_characters))
        myprint("Your target:", ' '.join(hidden_word))
        if '_' not in hidden_word:
            myprint("Great shot kid! That was one in a million:", word)
            myprint("Don't recognise the answer? Look it up on Wookipedia: https://starwars.fandom.com/wiki/Main_Page')")
            input('Press enter to start a new game:  \n')
            ("Starting your attack run .d..\n")
            play_the_game()
            break

    if attempts: 0
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

