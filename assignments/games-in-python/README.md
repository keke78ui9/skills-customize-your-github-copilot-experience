

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practice string manipulation, loops, conditionals, and user input while reinforcing problem-solving skills.

## 📝 Tasks

### 🛠️  Task 1: Set Up the Game

#### Description
Create the basic structure for your Hangman game, including a list of possible words and the logic to randomly select one for the player to guess.

#### Requirements
Completed program should:

- Define a list of at least 5 possible words
- Randomly select one word at the start of the game
- Display the number of letters in the word as underscores (e.g., _ _ _ _ _)

### 🛠️  Task 2: Implement Guessing Logic

#### Description
Allow the player to guess letters, track their progress, and manage the number of incorrect attempts.

#### Requirements
Completed program should:

- Accept single-letter guesses from the user
- Reveal correctly guessed letters in their positions
- Track and display the number of incorrect guesses remaining (e.g., 6 attempts)
- End the game when the word is fully guessed or attempts run out
- Display a win or lose message at the end

#### Example
```
Word: _ _ _ _ _
Guess a letter: a
Incorrect! Attempts left: 5
Word: _ _ _ a _
Guess a letter: t
Correct!
Word: _ _ t a _
...etc.
```
