# Welcome to Star Wars Hangman! 

For project three I decided to develop a Star Wars version of the hangman game, based on the films and TV shows. I chose this because I enjoy word word games and have been a Star Wars fan for as long as I can remember. This game brings both of those passions together and I have really enjoyed developing, testing and playing this game. 

## User Demographic
This game is aimed primarily at the following:
- people who enjoy Star Wars
- people who enjoy word games
- fans of pop culture
- anyone who wants to play a moderately challenging but not-too-taxing game on their phone during their commute, in their downtime, etc. 

## Purpose
The purpose of the game is:
- to test the player's depth of knowledge about Star Wars, from the well-known (Darth Vader and Grogu) to more obscure, deeper cuts (the Jedi called Yaddle, or the bar-tender Wuher)
- to offer the player a fun and relaxing pass-time 

# How the app works: overview
Although Hangman is a simple game to play, it is possible to add levels of difficulty. Do you, for example, strictly enforce a "10 attempt only" rule, including right and wrong guesses? In this scenario, the user has a strict number of attempts to get the answer, and each guess - right or wrong - uses up an attempt. Or do you allow the player to guess correctly without losing any attempts? This is the traditional Hangman gameplay, whereby no attempts are used up when the player guesses correctly; they only lose attempts for incorrect guesses.  

Although I originally planned to go for the strict '10 attempts only' option, I ended up developing the traditional gameplay with a couple of extra options to mix things up. The harder option could be added at a later date.  

As things stand now: the app / game works as follows: 
- all data for the answers, clues 1 and 2 are stored in the same worksheet in a linked google spreadsheet 
- details for the leaderboard are exported to the same spreadsheet but in a different worksheet and can be added to / viewed within the terminal at the player's request 
- from the homescreen, the user can choose to play the game, view the leaderboard or read the rules by entering 1, 2 or 3 on their keyboard (no other options are allowed)
- if the player chooses 1, the gameplay starts 
- if the player chooses 2, they are shown a leaderboard with the player's name, the answer they guessed, and how many chances are left over (see 'leaderboard' section for clarification)
- if the player chooses option 3, they are directed to a screen that explains how the game works and walks them through the process, explaining the different functionalities I've built into the game
- after this, the player is directed to press the 'enter' key to start the game 
- the game immediately shows the player a name with all letters replaced with an underscore: _
- if there are any hyphens or apostrophes in the name, these are displayed, e.g.
_ - _ _ _ _  (x-wing)
or 
_ _ _ _ _ '_  _ _ _ _ _ _ (jabba's palace)
- if the target is made up of more than one word, any spaces between the words are also displayed as spaces, e.g. _ _ _ &nbsp; &nbsp; _ _ _ _ (han solo)
- depending on the length of the word, the user has either six or ten 'wrong' guesses: this is defined in the 'play_the_game' function, and is currently set as follows: 6 characters in the name or fewer = 6 wrong guesses, and 7 characters or more = 10 wrong guesses 
- the user can enter a single question mark (?) for clue number one, which tells them if it is a character, a ship, an alien species, a place, a planet, a weapon or a creature. 
- asking for clue 1 uses up one attempt.  
- the user can then enter two question marks (??) for a second clue which tells them in which set of films or TV series the answer comes from, e.g. The Original Trilogy, Rebels, Ahsoka, The Prequels and The Clone Wars, etc. 
- asking for clue 2 uses up one attempt.   
- in the normal gameplay, the user can only enter one character at a time
- if the player guesses correctly, no attempts are lost 
- if the player guesses incorrectly, one attempt is lost 
- the user can also make a guess at the whole answer by entering an ! which triggers the option 'guess the answer', e.g. 'x-wing' or 'jabba's palace'.
- if they are right, they win
- if they are wrong, they use up one attempt  
- as long as they guess the answer before they have used up all their wrong guesses, they win
- if not, they lose
- if the player wins, they can decide to add their game to the leaderboard if they want to

# App functionality: in depth

## The Google Doc and API

![Linking the google doc](documentation/images/1_links_googledocs.PNG)

## My Print

I created a myprint for the Heroku terminal rather than using the standard 'print' because I wanted to give the terminal a left margin. I the text in the Heroku terminal difficult to read with the standard 'print' function so added a basic left margin with a new 'myprint' function coded as follows: 

![MyPrint](documentation/images/2_myprint.PNG)

The top line of the terminal (which I cannot change) shows it without a left margin, followed by my game which is all added with a left margin: 

![Left margin in terminal](documentation/images/2a_myprint_terminal.PNG)

## How to play: explanation
This is a sequence of statements added with myprint to explain the gameplay. I thought it would be good practice to add this in, especially to clarify what kinds of things the answers might be, to ask for the two clues and how to guess the whole answer:

![Gameplay](documentation/images/3_gameplay_explanation.PNG)

I added a 'clear screen' function here because I found the terminal too cramped when I went from the homescreen to the gameplay explanation. 

I found a solution on Stack Overflow which I used in my code - this is the source:
https://stackoverflow.com/questions/76955384/how-to-clear-the-screen-in-python-when-a-certain-condition-is-met-when-execution

![Clear Terminal](documentation/images/3a_clear-screen.PNG)


## Importing and displaying the target and clues 

In this section, I import the target from the google sheet:

![Import-target](documentation/images/4_import-word.PNG)

In my first tests of the game, I noticed that the capital letters I used while populating the spreadsheet were a problem, as were the occasional trailing spaces. Rather than edit the spreadsheet, I decided to eliminate both capitals and leading / trailing spaces by applying the lower and strip methods to the string.

I then applied the same approach to the imported clues:  

![Import-clues](documentation/images/5_import-clues.PNG)

For my own sake, it took some mental processing to understand how to import the correct clues based on the answer, but the process works reliably. As I understand the get_clue functions and would explain them: 
- the first line clue1_data refers to the linked spreadsheet 
- for row in clue1 data: word = row[0]: this refers to the target word that I am importing from the google doc and displaying the to player as underscores
- this 'word' has to be the same as the 'answer' parameter which is shown in parentheses = the target word which is shown to the player as underscores 
- as these have to be the same, row [1] (for Clue 1) has to refer to Clue1 in the linked spreadsheet, and row[2] has to refer to Clue2
- simply put: Python starts reading spreadsheets from row 0, so colum A = row 0, column B = row 1, and so on:

![Python-rows](documentation/images/5a_python-rows.PNG)

I cover the functionality around calling the clues in the 'Clues' section of this ReadMe below. 

## Setting up the game 
In this section I have defined some of the main variables for playing the game:

![Gameplay-variables](documentation/images/6_gameplay-and-variables.PNG)

Some clarifications: 
- Spaces, apostrophes and hyphens. I wanted to display hyphens, apostrophes and spaces as they are rather than hidden as underscores. I thought that asking the player to guess hyphens and apostrohes a little unfair, and would be inaccurate to some of the source material - I didn't want to display x wing or xwing which it is correctly x-wing. Additionally, showing spaces between words seemed only fair, which is why I added these three exceptions to the underscores here. 
- Guessed characters: I did not want to penalise the player who repeated a guess by mistake, so this variable keeps track of what they have guessed - correctly or incorrectly - and gives them a reminder in this case; additionally, they do not lose any attempts for repeated guesses. 
In this example, the player enters the letter Z twice, and gets the reminder on the second attempt:
![Repeat-guess](documentation/images/15_repeat-wrong-guess.PNG)
- Wrong guesses: to help the player keep track of where they are in the game, I use this variable to monitor their wrong guesses so I can display them to the player. I considered adding all guesses to this list, but as the correctly-guessed characters appear in the target word(s), this seemed redundant. 
![List-wrong-guesses](documentation/images/16_list-wrong-guesses.PNG)
- Invalid characters: it would be easy to lose an attempt by accidently entering a semi-colon, hash sign or asterisk, so I have excluded them where; if the user enters an invalid character, they get a warning message but they do not lose an attempt. 

This is the code that displays the corresponding error message: 

![Invalid-chars](documentation/images/8_invalid-chars.PNG)


- Clue1 and Clue 2: as Clue 1 is more general and Clue 2 more specific, I wanted to ensure that the player cannot ask for Clue 2 before Clue 1. Therefore I have set their default setting to 'False', and this becomes 'True' only when they have been called. This also facilitates the option to display the same clue a second or third time without the player losing an attempt (see 'Clue' section below)

## Number of attempts

I decided to implement a variable that allows the owner of the game to adapt the number of wrong guesses allowed per game. This is based on the length of the word: some names are very short, e.g. Rey, R2-D2, but I didn't want to exclude them as possible target answers. Equally, it seemed a bit unfair to have 10 attempts for this word - the same number as for 'Salacious B Crumb' - which is why I added this variable.  

![Nr-attempts](documentation/images/7_nr-attempts.PNG)

This could be adapted into a future iteration of the game, allowing the player to decide between easy, standard and hard difficulty levels based on the number of guesses, but I could not implement this at this stage.  

This returns me to a question I asked in the 'summary' of 'How the app works': what does an attempt mean? Does the player get 10 attempts in total, regardless if whether the guess is right or wrong, or does 10 attempts mean 10 wrong attempts? In the context of hangman, an attempt means a wrong guess, and so that is what it means here. But if I were to take this game any further, I would develop the naming coventions a little more to ensure 100% transparency.  

## Guess whole answer
As the rules of Hangman only allow one character at a time but also for the user to guess the whole answer, I needed a way to make both options acceptable. I enabled this function by allowing the user to enter a single exclamation mark (!) as a trigger to show the "Guess whole answer" input:

![Guess-whole-answer](documentation/images/9_guess-whole-answer.PNG)

![Guess-whole-answer-terminal](documentation/images/9a_guess-whole-terminal.PNG)

This allows me to enforce the 'one-character-at-a-time' Hangman rule, but also allows the player to guess the whole answer in one go.  

## Clues

As the Star Wars universe is quite vast, and the types of answers could include anything form planets to characters to creatures to spaceships, I decided to implement a 'get a clue' function: 
- clue 1 tells the player what the target is: whether it is a spaceship, character etc
- clue 2 tells the player in what series of films or TV shows the answer is most commonly found, e.g. The Original Trilogy, The Mandalorian, Kenobi, etc; if the answer is found in more than one series, I let the clue show the most common series the answer is found in, e.g. The Prequels and The Clone Wars.  
- each clue uses up one attempt 
- the player cannot get clue 2 until they have asked for clue 1: if they try, they get an error message but do not lose any attempts.
![Clue-1-first](documentation/images/10a_clue-1-first.PNG)

- if the player repeats a request for a clue, they do not lose any attempts. I found during testing that I would sometimes accidently enter ? rather than ?? when asking for clue 2, which is why I implemented this safety-net.
![Clue-repeat](documentation/images/10b_clue-repeat.PNG)

## Standard gameplay: 1 character only
In order to enforce the Hangman rule of 1 character per guess, I wrote this code to check the length of the input; with the exception of two question marks, this returns an error message if the player enters multiple characters. Additionally, it disables the possibility that the user enters a blank string by hitting the enter key; this issue with the enter key was a problem that I resolved with the help of my tutor, as I found it difficult to describe exactly what the enter key did, and therefore how to exclude it:
![1-char-only](documentation/images/11_1-char-only.PNG)

## Standard gameplay: correct and incorrect guesses 
Having covered the exceptions to the rules, we now come to the standard gameplay section. This is the code which governs what happens when the player guesses a single character:
![standard-play](documentation/images/12_standard-play.PNG)
If the guess is correct, each instance of its appearance in the word will be populated.
If the guess is incorrect, the the number of attempts is reduced by one, the guess is entered to the 'wrong guesses' list, and the user is told (i) the guess was wrong and (ii) how many attempts they have left.  

## End of game, win or lose
The functionality at the end of the game is basically the same regardless of whether the player wins or loses, with a couple of divergences:
![win](documentation/images/13_player-wins.PNG)

![lose](documentation/images/13_player-loses.PNG)
- in each case, the player is referred to the fan wiki "Wookipedia" to either find out more (if they won) or look up the answer (if they lost)
- in both cases, they can either play again or return to the homepage
- if the player loses, they can look at the leaderboard but not update it
- if the player wins, they can update the leaderboard; if they choose this option, it triggers an input field so they can enter their name. After that, they will be directed to the leaderboad where they can see the answer they guessed, and how many attempts are remaining
![input-name](documentation/images/17_leaderboard-name.PNG)

## The Leaderboard 
This was the last section of the app I put together. I created it for two reasons: 
- It's a good gameplay feature to include 
- I also wanted to practise exporting the results to an external spreadsheet as this is a common real-life request when, e.g. tracking sales, customer contacts etc.  

The functionality is reas



## Testing

| Test                                              | Expected outcome                                    | Result |
| ------------------------------------------------- | --------------------------------------------------- | ------ |	
|All pages: a custom 'myprint' version of 'print' displays all 'print' messages in the app  | lines are displayed in the Heroku Terminal with a slight left margin for readability | Pass   | 
|Homepage: type 1 and press enter                    | Loads and displays the game with message "Starting your attack run"	        | Pass   | 
|Homepage: type 2 and press enter                    | Loads and displays the leaderboard   	        | Pass  |
|Homepage: type 3 and press enter                    | Loads and displays the gameplay explanation   	        | Pass  |
|Homepage: enter any other characters than 1, 2 or 3     | Loads error message: 'No target found: please enter 1, 2 or 3'          | Pass   |    
|Homepage: error message after anything other than 1, 2 or 3 is entered    | Input field for options 1, 2 or 3 is visible and usable          | Pass   |    
|From homepage to gameplay page           | A single word - the 'target word' - is called at random from the linked Google doc 'answer' column  | Pass   |   	
|Gameplay page loads the 'target' word(s) | The target word is displayed with 'Your target:'       | Pass |
|Gameplay page loads the 'target' word(s) | All characters are hidden with underscores except for hyphens and apostrophes       | Pass | 
|Gameplay page loads the 'target' word(s) | Hyphens and apostrophes are displayed appropriately      | Pass | 
|Gameplay page loads the 'target' word(s) | Spaces between words are shown as spaces, not as underscores      | Pass | 
|Gameplay page loads the 'target' word(s) | The player is shown how many number of wrong guesses ('shots') they are allowed  | Pass |
|If the target word has 6 or fewer characters: | The user is told they have 6 wrong guesses ('shots') | Pass |
|If the target word has 7 or more characters: | The user is told they have 10 wrong guesses ('shots') | Pass |
|The values for length of word vs number of available guesses: | Changes to the variables in the code are reflected in the game   | Pass |
|Gameplay: the player enters a correct character: | Each instance of that character in the target is populated, 'Great shot' message shown | Pass |
|Gameplay: the player enters an incorrect character: | 'Missed' message is shown, the list of incorrect characters so far entered is shown | Pass |
|Gameplay: the player enters an incorrect character: | One attempt is lost, user us shown how many remaining attempts there are | Pass |
|Gameplay: the player tries to repeat a character they have already used, correctly or incorrectly: | 'Reminder' message is shown, user prompted to try something else | Pass |
|Gameplay: the player tries to repeat a character they have already used, correctly or incorrectly: | No attempts are lost | Pass |
|Gameplay: the player enters more than one character with exception of ??: | Error message is shown, no attempts are lost | Pass |
|Gameplay: the player enters more than one character with exception of ??: | User is reminded that they should enter ! to guess the whole answer | Pass |
|Gameplay: the player enters ! | The player is prompted to guess the entire answer | Pass |
|Gameplay: the player guesses the whole answer correctly | The game ends, user is congratulated | Pass |
|Gameplay: the player guesses the whole answer correctly | Link to Wookiepedia is shown | Pass |
|Gameplay: the player guesses the whole answer correctly | The player has options to play again, add their game to the leaderboard, or go to homepage | Pass |
|Gameplay: the player guesses the whole answer correctly and chooses to add game to leaderboard | A usable input field for their name is shown | Pass |
|Gameplay: the player guesses the whole answer correctly and chooses to add game to leaderboard | Name, guessed word and number of remaining wrong guesses are shown | Pass |
|Gameplay: the player guesses the whole answer correctly and chooses to add game to leaderboard | All details appear in the linked spreadsheet in the appropriate worksheet | Pass |
|Gameplay: the player guesses the whole answer incorrectly | The player is shown what they entered: they lose an attempt | Pass |
|Gameplay: the player guesses the whole answer incorrectly | The player can carry on playing unless they are out of chances | Pass |
|Gameplay: the player enters ? | Clue number 1 is called from the correct cell in the google sheet 'Clue 1' column and displayed the the user  | Pass |
|Gameplay: the player enters ? | An attempt is used up  | Pass |
|Gameplay: the player enters ?? | Clue number 2 is called from the correct cell in the google sheet 'Clue 2' column and displayed the the user  | Pass |
|Gameplay: the player enters ?? | An attempt is used up  | Pass |
|Gameplay: the player tries to call Clue 2 before Clue 1 | Error message is shown, player is prompted to call clue 1 first; no attempts are lost | Pass |
|Gameplay: the player enters any of the characters defined in the invalid_characters variable | An error message is shown, no attempts are lost  | Pass |
|Gameplay: the player tries to guess the whole answer at the start of the game before guessing any individual characters | The 'guess whole answer' prompt is correctly displayed and the function works correctly as described above | Pass |
|Gameplay: the player asks for Clue 1 at the start of the game before guessing any individual characters | Clue 1 is correctly displayed and the function works correctly as described above | Pass |
|Gameplay: the player can ask for Clue 1 and then guess the whole answer without guessing an individual character | Clue 1 functionality and Guess Whole Answer functionality work correctly as described above | Pass |
|Gameplay: the player can ask for Clue 1, Clue 2 and then guess the whole answer without guessing an individual character | Clue 1 and 2 functionality and Guess Whole Answer functionality work correctly as described above | Pass |
|Gameplay: the player can complete the game without asking for a clue or trying to guess the whole answer  | Standard gameplay functionality works as described above | Pass |
|Gameplay: each incorrect attempt and Clue reduces the number of available attempts by 1 until none are left | Player loses and is told they have lost against the Death Start  | Pass |
|Gameplay: player loses | Player is shown the correct answer and prompted to look it up on Wookiepedia | Pass |
|Gameplay: player loses | The player has options to play again, view the leaderboard, or go to homepage | Pass |
|Gameplay: player loses | All three options work | Pass |
|Gameplay: player wins | Player is congratulated and told they have won | Pass |
|Gameplay: player wins | Player is asked if they would like to find out more on Wookiepedia | Pass |
|Gameplay: player wins | The player has options to play again, add their game to the leaderboard, or go to homepage | Pass |
|Gameplay: player wins | Links to play again and homepage work | Pass |
|Gameplay: player wins and chooses to add their game to the leaderboard | A usable input field for their name is shown | Pass |
|Gameplay:  player wins | Name, guessed word and number of remaining wrong guesses are shown | Pass |
|Gameplay:  player wins | All details appear in the linked spreadsheet in the appropriate worksheet | Pass 
|Leaderboard: | Links to play again or homepage are shown and work | Pass 


## Bugs

TO BE COMPLETED 




Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
