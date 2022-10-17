# Roulette Game in Python

- [How does roulette work](##-How-does-roulette-work?)
- [Requirements](##-Requirements)

## How does roulette work?

At a casino, the roulette wheel is composed of alternating red and black slots, each slot with its own number. Prior to spinning the wheel, a player place a bet on a roulette table. They start with a fixed amount of money and bets a small part of this amount at each spin.
<br/>
The players objective is guess what number the roulette wheel will land on at each turn and, therefore, to win the most money. When the player has lost all their money, they are out of the game.

### Simulate a roulette game in Python

- The player bets on a single number between 0 and 49. While they choose their number, they also choose the amount of money to play.

- The script generates a random number in this range (0 - 49), simulating the roulette. If the output number is the same than the number that was chosen (1/50 probability), then the player has won FIFTY times their bet!

- If not, the player loses their bet and can try again in the next round.  

- If the user is running out of money, the script stops and displays that they have lost.

### Further instructions

- When the player bets an amount of money, you have to check to ensure this corresponds with the amount of money the player has left. You also have to check that this amount is greater than 0. You will ask them as long as these conditions are not met.

- When the player bets a number, the program has to check that the number is between 0 and 49.

## Requirements

To run the Roulette Game you need to have Python installed (if you don't click [here](https://www.python.org/downloads/) to install).
The next step is installing the Python package installer pip ([click here](https://pip.pypa.io/en/stable/)) to get the following items by typing:

`pip install desired_package`

- Inquirer
- Random

## Instructions

The game starts with a brief description of the rules and asks for the user to choose a number. If the number is in a valid range (between 0 and 49) then it asks to input the bet value for the current round. The second output must be lower than the initial value given to the user.