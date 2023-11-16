# Guess the Number Game

This is a simple console-based "Guess the Number" game implemented in Python. The game consists of multiple levels with decreasing ranges and lives. The player has to guess the correct number within the given range to proceed to the next level.

## How to Play

1. Run the script in a Python environment.
2. The game will start with Level 0, and the player needs to guess the correct number within the specified range to move on to the next level.
3. For each level, the range decreases, and lives are adjusted accordingly.
4. Input your guesses when prompted and receive feedback on whether the number is higher or lower.
5. Complete all levels to finish the game.

## Functions

### `input_num(range_num)`

- Takes the range of numbers as input.
- Gets the player's input for their guess within the specified range.

### `catch_me(usr_input, range_num)`

- Verifies that the player's input is an integer within the acceptable range for the level.
- Prompts the player for a new input if the provided input is not valid.

### `check_in(range_num, usr_input, attempts, lives, lvl)`

- Implements the core logic of the game.
- Generates a random number within the given range.
- Allows the player to guess the number, providing feedback and adjusting lives.
- Exits the game if lives are exhausted or the player completes all levels.

### `choices(lvl)`

- Asks the player if they want to play again or exit after completing Level 3.

### `complete_all_levels()`

- Starts the game by initializing levels, lives, and ranges.
- Calls other functions to facilitate the gameplay.

### `test_check()`

- Tests the `check_in` function with predefined inputs and expected results.

## How to Run Tests

Uncomment the `test_check()` function call at the end of the script to run the test. Ensure that the game is not running while testing.

**Note:** This game is designed for educational purposes and may require additional enhancements for a more polished gaming experience.