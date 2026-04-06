JOURNAL.md
### **New Interaction**
- **Date**: 04-06-2026 23:21
- **User**: afina.kholidi@epita.fr
- **Prompt**: User asked: "looking through my entire lab folder, is everything in order?" and I performed various checks on the files, ran tests, checked git status, etc.
- **CoPilot Mode**: Ask
- **CoPilot Model**: Grok Code Fast 1
- **Changes Made**: No changes made; user performed checks on files, ran tests, and checked git status.
- **Context and Reasons for Changes**: The user was verifying the state of their lab folder to ensure everything is in order, including file integrity, test results, and version control status.
- **My Observations**:
This file serves as a comprehensive log of all prompts, responses, changes made, and reflections during the development process. Each entry is listed in reverse chronological order, with the most recent interactions at the top.

2026-03-12
Phase 7 – Constraint Compliance Refactoring

Refactored main.py to remove all `while True` loops (strictly forbidden by assignment constraints).

Input Validation Loop in play_game():
  - OLD: while True with break on valid input
  - NEW: guess = "" followed by while not (len(guess) == 1 and guess.isalpha())
  - Logic unchanged: validates single alphabetic characters
  - Same error message and flow

Play Again Loop in entry point:
  - OLD: while True with break on valid response
  - NEW: response = "" followed by while response not in ['y', 'n']
  - Logic unchanged: accepts 'y' or 'n' (case-insensitive)
  - Same error message and flow
  - Set play_again after loop completes

Verification:
  - Both conditional loops exit when their conditions are satisfied
  - No break statements used
  - Explicit loop conditions replace hidden breaks
  - Game behavior remains identical
  - Code is now fully compliant with assignment constraints

2026-03-12
Phase 6 – Final Implementation & Documentation

Implemented get_display_word(secret_word, guessed_letters):
  - List comprehension: shows char if non-alphabetic OR in guessed_letters, else "_"
  - Joins with spaces for readability: "h _ _ l o"
  - Handles non-alphabetic characters (spaces, hyphens) by always revealing them
  - Example: get_display_word("hello-world", ['h', 'e']) → "h e _ _ _ - _ _ _ _ _"

Implemented play_game(secret_word) orchestrator:
  - Initializes lives = 6, guessed_letters = []
  - Main loop: while lives > 0 and not game_won
  - Displays current word state, lives, and guessed letters before each prompt
  - Input validation loop (rejects non-alpha or multi-character input, no turn penalty)
  - Calls update_game_state() for state transitions
  - Detects win with: "_" not in get_display_word() (reuses display logic)
  - Returns boolean: True for win, False for loss

Implemented load_word() helper:
  - Attempts to read random word from words.txt
  - Falls back to hardcoded list ['epita', 'python', 'cybersecurity', 'quantum']
  - Ensures game never crashes due to missing word source
  - Returns a string (a single word)

Implemented entry point (if __name__ == "__main__"):
  - Welcomes player
  - Outer loop: while play_again
  - Calls load_word() to get secret word
  - Calls play_game(secret_word) and captures result
  - Displays: "Congratulations! You guessed it: [WORD]" if won, else "Game Over! The word was: [WORD]"
  - Prompts "Play again? (y/n):" with validation loop
  - Exits with "Thanks for playing!" when player chooses not to replay

Updated Documentation:
  - README.md: Complete rewrite describing the Hangman game, features, architecture, design decisions, and testing examples
  - REPORT.md: Comprehensive reflection document covering initial thoughts, learnings, CoPilot experience, AI trust patterns, and project reflection
  - MY_NOTES.md: Added implementation details for get_display_word and clarified edge cases

2026-03-12
Phase 5 – Architecture & Implementation of `get_display_word()`

Reviewed `update_game_state()` function for edge cases and return value design.
Confirmed design decisions:
  - Input validation happens in UI layer before calling state functions.
  - `update_game_state()` handles only mechanics: returns (guessed_letters, lives).
  - Win/lose checks and game loop orchestration live in `play_game()`.
  - Duplicate guesses are caught early (return early without changing state).
  
Designed `get_display_word()` function:
  - Preserves original casing while checking against lowercase normalized guessed_letters.
  - Non-alphabetic characters (spaces, hyphens) are always revealed for structure clarity.
  - Display uses spaces between characters: "h _ _ l o".
  - Implemented with list comprehension and `char.isalpha()` check.

Confirmed architecture:
  - `play_game()`: Orchestrator for one complete round (validates input, calls state/display functions, checks termination).
  - Entry point (`if __name__ == "__main__"`): Handles replay logic and meta-level game flow.
  - Loop condition explicit: `while lives > 0 and not game_won:`.
  - Separation of concerns: mechanics, presentation, orchestration, and entry point are distinct.

2026-03-12
Phase 4 – Full Game Loop

Implemented game_turn as a recursive function (no while True).
Implemented get_player_guess with recursive input validation.
Implemented run entry point with replay support (no program restart needed).
Implemented display_status — UI fully separated from logic layer.
Verified all constraints: no while True , no str.replace , replay , logic/UI split .

Phase 3 – Documentation & Testing

Asked CoPilot to review and document main.py. Accepted docstrings; skipped trivial one-liners.
Wrote test_game.py with 16 unit tests covering correct/wrong/duplicate guesses, win/loss detection, masked word, incorrect guesses list.
All 16 tests pass with python test_game.py.

Phase 2 – Core Logic

Implemented update_game_state manually without CoPilot.
Pure function: no loops, no global state, inputs treated as immutable.
Asked CoPilot (Ask Mode) to review — suggested adding lowercase normalisation; applied in UI layer to keep logic pure.

Phase 1 – Design Thinking

Wrote design notes in MY_NOTES.md: states, variables, rules/invariants, bugs/edge cases.
Consulted CoPilot (Ask Mode) on the same four questions and compared answers.
Selected relevant suggestions; added them under "CoPilot Suggestions" in MY_NOTES.md.