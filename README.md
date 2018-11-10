# Pig Dice Game
By Cliff Nyendwe, 29/09/2018
# Description
A pplication where two users can play a game of Pig Dice against each other. Pig Dice is a game where each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold"
# Specs of the program
The application works as follows:

It can generate a random number between 1-6(Numbers on sides of a dice)

* Example Input : User taps ROLL button
* Example Output: 5 (Number 5 is randomly generated)
* The random number generated once the user ROLLs die is added to their turn total.

* Example Input : 5 (Number from spec one)
* Example Output: 5 (0 + 5)
* The turn total continues to increase as the user continues rolling the die.

* Example Input: 6 (Number generated after user taps rolls dies again)
* Example Output: 11 (5+6)
* The turn total falls to zero '0' if the user ROLLs a 1.

* Example Input : 1 (User rolls 1)
* Example Output: 0 (11*0)
* It becomes the next player's turn if the current user rolls a 1.

* Example Input : Player One (Player One's turn before they rolls a one)
* Example Output: Player Two (Player Two's turn after Player One rolls a one)
* It becomes the next player's turn if they decide to hold.

* Example Input : Player Two taps HOLD during their turn
* Example Output: Player One (It's now player one's turn)
* It adds the current players turn total to their total score if they tap HOLD

* Example Input: Total Score = 0 Turn Total = 20 (Total Score and Turn Total before holdig)
* Example Output: Total Score = 20 Turn Total = 0 (Total Score and Turn Total after holding)
* When either player's total Score reaches 100, game is stopped and the winner is announced

* Example Input : Player Two's Total Score = 100
* Example Output: Player Two CONGRATS,YOU WIN.
* A new round of Pig Dice is started when either user taps NEW GAME, all scores are reset

* Example Input : tap NEXT GAME
* Example Output: Scores Reset, New Gam

# Github-link
https://github.com/cliffnyendwe/pig-dice-game.git

# Contacts
To find me, use: cliffnyendwe2018@gmail.com 0710755176

# Code Example
Kindly to access code clone the repository.

# Motivation
To make it easy for people to understand javascript knowledge and be able to put it into use by coming with games like pig dice game.

# Language used
HTML CSS JavaScript

# License
The project is under license by MIT

# Prerequisites
You will need the following things properly installed on your computer.

* atom
* git
* github