# My Original Thinking
## What ares the states of a game like Hangman?


- **GAMEPLAY LOOP**: Loading of guessable word, Player guesses letter-by-letter until all letters are found, congratulations +final word reveal
- **REPLAY?**: After win/loss, the user is offered to start over with a different word. Yes -> restart gameplay loop, No -> quit.

## What variables are required?

- **`secret_word`**: The target word, chosen randomly from a list of words
- **`guessed_letters`**: all the user guesses/inputs (letters)
- **`lives`**: Number of incorrect guesses remaining (integer, starts at 6)
- **`display_word`**: Masked representation shown to player (string with spaces and underscores)

## What are the rules and invariants?

Game mechanics and constraints:

- The secret word contains only characters from "a-z" (upper/lower)
- Lives is a positive integer
- **A life is deducted only for NEW incorrect guesses**, not duplicates
- Duplicate guesses produce no state change and no penalty
- Input is always normalized to lowercase for consistent comparison
- Non-alphabetic characters in secret_word (spaces, hyphens) are always revealed

## Bugs and Edge Cases

- **Inputting Multiple characters instead of just one**: Reject without penalty
- **Non-alphabetic characters**: Reject without penalty
- **Empty input**: Reject without penalty
- **Uppercase/lowercase**: Normalize to lowercase immediately
- **Duplicate guesses**: No penalty
- **Final guess with 1 life remaining**: Correctly deduct the life and end game

# COPILOT ANSWERS

## 1. App States
* **Initialization**: The script starts, prints a welcome message, and enters the primary loop.
* **Word Selection**: The load_word() function executes to retrieve a secret word from words.txt or the fallback_words list.
* **Active Gameplay**: The play_game() function manages the sub-loop where the player inputs letters and the game state updates.
* **Resolution**: The game evaluates the exit condition (either lives == 0 or game_won == True), displays the final result, and prompts for a restart.

## 2. App Variables
Variables are well-named and serve distinct purposes within the logic:

| Variable | Scope | Purpose |
| secret_word | Global/Local | The target word the player is trying to guess. |
| guessed_letters | play_game | A list containing all characters the player has already attempted. |
| lives | play_game | An integer counter (starting at 6) tracking remaining attempts. |
| game_won | play_game | A boolean flag used to break the game loop upon victory. |
| current_display | play_game | The string representation of the word (e.g., p _ t h _ n). |
| play_again | __main__ | A boolean controlling the high-level application loop. |

## 3. App Rules and Invariants

* **Case Insensitivity**: All inputs and comparisons are normalized using .lower(), ensuring 'A' and 'a' are treated identically.
* **Strict Input Validation**: The user must provide exactly one alphabetic character; otherwise, the game state does not progress.
* **Conditional Life Deduction**: lives only decreases if the guess is both new (not in guessed_letters) and incorrect (not in secret_word).
* **Idempotency**: Re-guessing a letter already in guessed_letters results in no penalty and no change to the state.
* **Winning Invariant**: The game is won if and only if the current_display contains no underscore characters.

## 4. App Bugs and Potential Improvements

### Double Display Redundancy
In play_game, current_display is calculated twice per loop iteration (once at the start to show the user, and once at the end to update game_won). This is redundant processing.

### Efficiency in update_game_state
The code uses list concatenation: new_guessed_letters = guessed_letters + [low_guess]. In Python, this creates a brand-new list every time, which is an O(n) operation. Using a Set for guessed_letters would provide O(1) lookup times and handle duplicates more idiomatically.

### Non-Alphabetic Secret Words
If words.txt contains a word with a space or a hyphen (e.g., "ice-cream"), the get_display_word logic handles this correctly by displaying non-alpha characters immediately. The winning condition remains robust because it only looks for the absence of underscores.

### Redundant String Processing
The secret_word.lower() call happens every time a user makes a guess. It is more efficient to call .lower() once inside load_word() or at the very start of play_game().

## MY OBSERVATIONS : 

CoPilot goes into much more depth to optimize for lower processing power usage, for example looking into reordering different steps of the way. It also looks for much more diverse and "niche" edge cases to push the code to its limits. So also it is more complicated in everything it does, it is not excessive, as it strictly stayed in the bounds of the project.

It is helpful because a normal human will never go into so much depth to ensure safety and fully functioning code : As for a human tests mostly for "human" cases. An example of this, is following instructions. If the user is asked to enter a single character, the human will test for every different character of the alphabet, but might not create a case for when the input is not included in a-z || A-Z. Additionally, CoPilot can compare different versions of a same program much quicker to find the optimized approach to a solution. Therefore it is a very helpful tool to keep on the side.
