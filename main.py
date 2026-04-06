import random
import time

def update_game_state(secret_word, guessed_letters, guess, lives):
    """Updates the game state based on the user's guess."""
    low_guess = guess.lower()

    if low_guess in guessed_letters:
        return guessed_letters, lives

    new_guessed_letters = guessed_letters + [low_guess]

    if low_guess not in secret_word.lower():
        return new_guessed_letters, lives - 1

    return new_guessed_letters, lives


def get_display_word(secret_word, guessed_letters):
    """Creates a string representing the current progress of the word."""
    display = [
        char if not char.isalpha() or char.lower() in guessed_letters 
        else "_" 
        for char in secret_word
    ]
    return " ".join(display)


def get_computer_guess(guessed_letters):
    """
    Returns the most common English letter that hasn't been guessed yet.
    Strategy: ETAOIN SHRDLU (English letter frequency)
    """
    frequency_order = "etaoinshrdlcumwfgypbvkjxqz"
    for letter in frequency_order:
        if letter not in guessed_letters:
            return letter
    return None


def play_game(secret_word, auto_play=False):
    """Manages the main loop for a single round of hangman."""
    lives = 6
    guessed_letters = []
    game_won = False
    
    while lives > 0 and not game_won:
        current_display = get_display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Lives remaining: {lives}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        if auto_play:
            # Add a small pause so the user can follow the computer's logic
            time.sleep(1) 
            guess = get_computer_guess(guessed_letters)
            print(f"Computer guesses: {guess}")
        else:
            guess = ""
            while not (len(guess) == 1 and guess.isalpha()):
                guess = input("Guess a letter: ").strip().lower()
                if not (len(guess) == 1 and guess.isalpha()):
                    print("Invalid input. Please enter a single letter.")
        
        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)
        
        # Check if the player has uncovered the whole word
        current_display = get_display_word(secret_word, guessed_letters)
        game_won = "_" not in current_display
    
    return game_won


def load_word():
    """Attempts to load a random word from an external text file or fallback list."""
    fallback_words = ['epita', 'python', 'cybersecurity', 'quantum', 'vibecoding']
    try:
        with open('words.txt', 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        if words:
            return random.choice(words)
    except FileNotFoundError:
        pass
    return random.choice(fallback_words)


if __name__ == "__main__":
    print("--- Welcome to Hangman ---")
    
    # Selection of Game Mode
    mode = ""
    while mode not in ['1', '2']:
        mode = input("Select Mode:\n(1) Human Player\n(2) Auto-Play (Computer)\nChoice: ").strip()
    
    is_auto = (mode == '2')
    play_again = True
    
    while play_again:
        secret_word = load_word()
        won = play_game(secret_word, auto_play=is_auto)
        
        if won:
            print(f"\nVictory! The word was: {secret_word}")
        else:
            print(f"\nGame Over! The word was: {secret_word}")
        
        response = ""
        while response not in ['y', 'n']:
            response = input("\nPlay again? (y/n): ").strip().lower()
        
        play_again = (response == 'y')
    
    print("Thanks for playing!")