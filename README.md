# Hangman Word Game

## Project Overview

This is a terminal-based Hangman game written in Python. The player must guess the secret word one letter at a time. Correct guesses reveal letters in the word, while incorrect guesses reduce the available lives. The game ends when the word is fully revealed or when the player runs out of lives.

## Features

- Single-letter input validation
- Case-insensitive guessing
- Duplicate guesses are ignored without losing a life
- Word display shows underscores for hidden letters and reveals non-alphabetic characters immediately
- Automatic fallback word selection if `words.txt` is missing
- Replay support after each game ends

## Files

- `main.py` — main game implementation
- `hangman_testing.py` — unit-style tests for the core guess handling logic
- `README.md` — project instructions and overview
- `REPORT.md` — project reflection and development notes
- `MY_NOTES` — author notes on design decisions and game state
- `JOURNAL.md` — development log and activity history

## Usage

From the project root folder, run:

```bash
python main.py
```

If you want to stop playing after a round, choose `n` when prompted.

## Testing

Run the test script from the project root:

```bash
python hangman_testing.py
```

Expected output:

```text
Test 1 Passed: Correct guess handled.
Test 2 Passed: Incorrect guess deducted life.
Test 3 Passed: Duplicate guess ignored.
Test 4 Passed: Case sensitivity handled.

All tests passed successfully!
```

## How it works

1. The game loads a secret word from `words.txt`, if available.
2. If the file is missing, a fallback list of words is used.
3. The player guesses letters until they either uncover the full word or lose all lives.
4. The game ignores invalid input and duplicate letters.
5. After the round, the player can choose to play again.

## Notes

- The game expects alphabetic letter guesses only.
- The display is case-insensitive, but the word is shown using its original characters.
- Use a `words.txt` file in the project folder to customize the selectable word list.

## Requirements

- Python 3.x

Enjoy the game!