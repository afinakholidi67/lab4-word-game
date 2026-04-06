import random

def update_game_state(secret_word, guessed_letters, guess, lives):
    """
    Updates the game state based on the user's guess.
    
    Args:
        secret_word (str): The target word to guess.
        guessed_letters (list): List of letters already guessed.
        guess (str): The current letter being guessed.
        lives (int): Current number of attempts remaining.
        
    Returns:
        tuple: (Updated list of guessed letters, updated lives count)
    """
    low_guess = guess.lower()

    # If the letter was already guessed, return the state unchanged
    if low_guess in guessed_letters:
        return guessed_letters, lives

    # Append the new guess to the history
    new_guessed_letters = guessed_letters + [low_guess]

    # Deduct a life if the guess is not in the secret word
    if low_guess not in secret_word.lower():
        return new_guessed_letters, lives - 1

    return new_guessed_letters, lives


def get_display_word(secret_word, guessed_letters):
    """
    Creates a string representing the current progress of the word.
    
    Args:
        secret_word (str): The word to display.
        guessed_letters (list): Letters that have been correctly guessed.
        
    Returns:
        str: The word with unguessed letters as underscores, separated by spaces.
    """
    # Show the character if it is non-alphabetic or has been guessed; else show "_"
    display = [
        char if not char.isalpha() or char.lower() in guessed_letters 
        else "_" 
        for char in secret_word
    ]
    return " ".join(display)


def play_game(secret_word):
    """
    Manages the main loop for a single round of hangman.
    
    Args:
        secret_word (str): The word the player needs to guess.
        
    Returns:
        bool: True if the player won, False if the player lost.
    """
    lives = 6
    guessed_letters = []
    game_won = False
    
    while lives > 0 and not game_won:
        # 1. Display current progress
        current_display = get_display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Lives remaining: {lives}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        # 2. Get and validate user input
        guess = ""
        while not (len(guess) == 1 and guess.isalpha()):
            guess = input("Guess a letter: ").strip()
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid input. Please enter a single letter.")
        
        # 3. Update the game state (letters and lives)
        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)
        
        # 4. Check if the player has uncovered the whole word
        current_display = get_display_word(secret_word, guessed_letters)
        game_won = "_" not in current_display
    
    return game_won


def load_word():
    """
    Attempts to load a random word from an external text file.
    Falls back to a hardcoded list if the file is missing or empty.
    
    Returns:
        str: A random word selected for the game.
    """
    fallback_words = ['epita', 'python', 'cybersecurity', 'quantum', 'vibecoding']
    
    try:
        with open('words.txt', 'r') as f:
            # Create a list of words, removing whitespace and empty lines
            words = [line.strip() for line in f if line.strip()]
        
        if words:
            return random.choice(words)
    except FileNotFoundError:
        # If words.txt is missing, we proceed to return from fallback_words
        pass
    
    return random.choice(fallback_words)


if __name__ == "__main__":
    print("Welcome to Hangman!")
    
    play_again = True
    while play_again:
        # Load a new word and start the game loop
        secret_word = load_word()
        won = play_game(secret_word)
        
        # Provide final results
        if won:
            print(f"\nCongratulations! You guessed it: {secret_word}")
        else:
            print(f"\nGame Over! The word was: {secret_word}")
        
        # Prompt user to restart or exit
        response = ""
        while response not in ['y', 'n']:
            response = input("\nPlay again? (y/n): ").strip().lower()
            if response not in ['y', 'n']:
                print("Please enter 'y' or 'n'.")
        
        play_again = (response == 'y')
    
    print("Thanks for playing!")