## Welcome to Star Wars Hangman! 

For project three I decided to develop a Star Wars version of the hangman game, based on the films and TV shows. I chose this because I enjoy word word games and have been a Star Wars fan for as long as I can remember. This game brings both of those passions together and I have really enjoyed developing, testing and playing this game. 

## User Demographic
This game is aimed primarily at the following:
- people who enjoy Star Wars
- people who enjoy word games
- fans of pop culture
- anyone who wants to play a moderately challenging but not-too-taxing game on their phone during their commute, in their downtime, etc. 

## Purpose
The purpose of the game is:
- to test the player's depth of knowledge about Star Wars, from the well-known (Darth Vader and Grogu) to more obscure, deeper cuts (the Jedi called Yaddle, or member of the Rebellion called Ruescott Melshi)
- to offer the player a fun and relaxing passtime 

## How to play: summary
The gameplay is fairly simple, as befits a hangman game, but I have added a couple of extra options to mix things up. The game works as follows: 

- from the homescreen, the user can choose to play the game or read the rules by entering '1' or '2' on their keyboard (no other options are allowed)
- if the player chooses option 2, they are directed to a screen that explains how the game works and walks them through the process, explaining the different functionalities I've built into the game
- after this, the player is directed to press the 'enter' key to start the game 
- the game immediately shows the player a name with all letters replaced with an underscore: _
- if there are any hyphens or apostrophes in the name, these are displayed, e.g.
_ - _ _ _ _
or 
_ _ _ _ _ '_  _ _ _ _ _ _
- if the target is made up of more than one word, any spaces between the words are also displayed as spaces 
- depending on the length of the word, the user has either six or ten 'wrong' guesses: this is defined in the 'play_the_game' function, and is currently set as follows: 6 characters in the name or fewer = 6 wrong guesses, and 7 characters or more = 10 wrong guesses 
- the user can enter a single question mark (?) for clue number one, which tells them if it is a character, a ship, an alien species, a place, a planet, a weapon or a creature of some description. This also uses up one attempt.  
- the user can then enter two question marks (??) for a second clue which tells them in which set of films or TV series the answer comes from, e.g. The Original Trilogy, Rebels, Ahsoka, The Prequels and The Clone Wars, etc. This uses up one attempt. 
- in the normal gameplay, the user can only enter one character at a time
- however, the user can make a guess at the whole answer by entering an ! which triggers the option 'guess the answer', e.g. 'x-wing' or 'jabba's palace'.
- if they are right, they win
- if they are wrong, they use up one attempt  
- as long as they guess the answer before they have used up all their wrong guesses, they win
- if not, they lose




## Testing

| Test                                              | Expected outcome                                    | Result |
| ------------------------------------------------- | --------------------------------------------------- | ------ |	
|All pages: a custom 'myprint' version of 'print' displays all 'print' messages in the app  | lines are displayed in the Heroku Terminal with a slight left margin for readability | Pass   | 
|Homepage: type 1 and press enter                    | Loads and displays the game with message "Starting your attack run"	        | Pass   | 
|Homepage: type 2 and press enter                    | Loads and displays the gameplay explanation   	        | Pass  |
|Homepage: enter any other characters than 1 or 2     | Loads error message: 'No target found: please enter 1 or 2'          | Pass   |    
|Homepage: error message after anything other than 1 or 2 is entered    | Input field for option 1 or 2 is visible and usable          | Pass   |    
|From homepage to gameplay page           | A single word - the 'target word' - is called at random from the linked Google doc 'answer' column  | Pass   |   	
|Gameplay page loads the 'target' word(s) | The target word is displayed with 'Your target:'       | Pass |
|Gameplay page loads the 'target' word(s) | All characters are hidden with underscores except for hyphens and apostrophes       | Pass | 
|Gameplay page loads the 'target' word(s) | Hyphens and apostrophes are displayed appropriately      | Pass | 
|Gameplay page loads the 'target' word(s) | Spaces between words are shown as spaces, not as underscores      | Pass | 
|Gameplay page loads the 'target' word(s) | The player is shown how many number of wrong guesses ('shots') they are allowed  | Pass |
|If the target word has 6 or fewer characters: | The user is told they have 6 wrong guesses ('shots') | Pass |
|If the target word has 7 or more characters: | The user is told they have 10 wrong guesses ('shots') | Pass |
|Gameplay: the player enters a correct character: | Each instance of that character in the target is populated, 'Great shot' message shown | Pass |
|Gameplay: the player enters an incorrect character: | 'Missed' message is shown, the list of incorrect characters so far entered is shown | Pass |
|Gameplay: the player tries to repeat a character they have already used, correctly or incorrectly: | 'Reminder' message is shown, user prompted to try something else, no attempts lost | Pass |
|Gameplay: the player enters an incorrect character: | One attempt is lost, user us shown how many remaining attempts there are | Pass |
|Gameplay: the player enters more than one character with exception of ??: | Error message is shown, no attempts are lost | Pass |
|Gameplay: the player enters more than one character with exception of ??: | User is reminded that they should enter ! to guess the whole answer | Pass |
|Gameplay: the player enters ! | The player is prompted to guess the entire answer | Pass |
|Gameplay: the player guesses the whole answer correctly | The game ends, user is congratulated | Pass |
|Gameplay: the player guesses the whole answer correctly | Link to Wookiepedia is shown | Pass |
|Gameplay: the player guesses the whole answer correctly | The player is prompted to play again by pressing the enter key | Pass |
|Gameplay: the player guesses the whole answer incorrectly | The player is shown what they entered: they lose an attempt | Pass |
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
|Gameplay: player loses | Player is prompted to play again by pressing the enter key | Pass |
|Gameplay: player wins | Player is congratulated and told the have won | Pass |
|Gameplay: player wins | Player is asked if they would like to find out more on Wookiepedia | Pass |
|Gameplay: player wins | Player is prompted to play again by pressing the enter key | Pass |

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
