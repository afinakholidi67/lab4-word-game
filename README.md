# Hangman Word Game

A Python implementation of the classic Hangman game, built with a focus on clean architecture, separation of concerns, and maintainability.

## Overview

This project demonstrates software engineering best practices through a word-guessing game where:
- The player has 6 attempts to guess letters in a secret word
- Non-alphabetic characters (spaces, hyphens) are always revealed to aid guessing
- The display updates after each guess with the current word state and remaining lives
- Input validation ensures only single letters are processed
- The player can replay without restarting the program

## Features

- **Pure State Transitions**: `update_game_state()` handles only game mechanics without side effects
- **Display Separation**: `get_display_word()` manages the UI layer independently
- **Modular Game Loop**: `play_game()` orchestrates one complete round
- **Word Loading**: `load_word()` reads from a word list with graceful fallback
- **Replay Support**: Main entry point handles multiple games in one session
- **Input Validation**: Rejects invalid input without penalizing the player

## Usage

### Basic Game
```sh
python main.py
```

Follow the on-screen prompts to:
1. Guess letters one at a time
2. Try to reveal the entire word before running out of lives
3. Play again or exit when prompted

### Custom Word List
Create a `words.txt` file with one word per line:
```
python
cybersecurity
quantum
algorithm
```

If `words.txt` is missing or empty, the game falls back to a hardcoded list.

## Project Structure

### Core Functions

- **`update_game_state(secret_word, guessed_letters, guess, lives)`**
  - Pure function handling game mechanics
  - Returns updated `guessed_letters` and `lives`
  - Returns early for duplicate guesses (no penalty)

- **`get_display_word(secret_word, guessed_letters)`**
  - Renders the masked word for display
  - Preserves original casing while checking normalized state
  - Always reveals non-alphabetic characters (spaces, hyphens, etc.)
  - Example: `get_display_word("hello-world", ['h', 'e'])` → `"h e _ _ _ - _ _ _ _ _"`

- **`play_game(secret_word)`**
  - Orchestrates one complete game round
  - Manages the main game loop: `while lives > 0 and not game_won:`
  - Validates input (single alphabetic character)
  - Returns `True` if player won, `False` if lost

- **`load_word()`**
  - Reads a random word from `words.txt`
  - Falls back to hardcoded list if file is missing or empty
  - Ensures the game never crashes due to missing word source

### Entry Point
- **`if __name__ == "__main__":`**
  - Handles replay loop
  - Displays win/loss messages with the revealed word
  - Prompts for replay after each game

## Design Decisions

### Architecture
- **Input Validation**: Happens in the UI layer before state updates (no penalties for typos)
- **State vs. Display**: Internal state is normalized (lowercase); display preserves original casing
- **Single-Round Design**: `play_game()` handles exactly one game, making it testable and reusable
- **Loop Condition**: Explicit termination (`while lives > 0 and not game_won`) instead of hidden breaks

### Game Rules
- Player starts with **6 lives**
- Guessing a letter already entered: no penalty, no state change
- Guessing a wrong letter: lose 1 life
- Guessing a correct letter: reveal all instances in the word
- **Win**: All letters in the word are guessed
- **Loss**: Lives reach 0 before completing the word

## Files

- [`main.py`](main.py): Complete game implementation
- [`words.txt`](words.txt) *(optional)*: Custom word list (one word per line)
- [`REPORT.md`](REPORT.md): Learnings and reflections on the project
- [`JOURNAL.md`](JOURNAL.md): Detailed interaction log with AI

## Testing

To verify the core functions work correctly:

```python
# Test state transitions
guessed, lives = update_game_state("hello", [], "e", 6)
print(guessed)  # ['e']
print(lives)    # 6 (correct guess, no penalty)

# Test display
display = get_display_word("hello", ['h', 'e'])
print(display)  # "h e _ _ _"

# Test with special characters
display = get_display_word("hello-world", ['h', 'e'])
print(display)  # "h e _ _ _ - _ _ _ _ _"
```

## Learning Outcomes

This project demonstrates:
- Clean separation of concerns (state, display, orchestration)
- Pure functions and immutable data handling
- Input validation and error handling
- Modular design for testability and reusability
- Effective use of AI tools for guided learning

## Custom Instructions & Journal Logger Agent

This repository uses configuration files to guide AI interactions:

- **Custom Instructions**: `.github/copilot-instructions.md`
  - Defines project-specific rules for Copilot
  - Ensures responses follow tutor mode and journaling requirements

- **Journal Logger Agent**: `.github/agents/journal-logger.agent.md`
  - Automatically logs interactions with AI in `JOURNAL.md`
  - Maintains a comprehensive history of prompts, responses, and code changes

---

## Students Comments

Thank you for using this project as a learning resource!

- Athena: Successfully completed the project with a clean, modular architecture.
- MUHAMMAD Ahtisham Asghar: Hello, I'm excited to learn about git & version control!
- Abdullah Salman: Hello, I am excited to learn about git and version control
- Justin D'COSTA: Bonjour!
- Fathima Gafoor : Hello , i am excited to improve practical Git skills
- Success Aderibigbe : Im so GOATED
- Redowan Ahmed SAMEER: Hello, I am excited to improve practical Git skills.
- Demod Singh Tamang : Groot!
- Michee - Lucas Izambay: Wazzup
- [Artem I]: Am I doing this correctly?
- Abdulaziz Eusman: Solo leveling is mid.
- Yuchen: Hi!
- Busra: This is fun :D
- Arkar Thurein: Excited to start working with Python and Git!
- Nidhish Srinivasan Krishnassamy: Excited to start learning Git, Python and AI tools

