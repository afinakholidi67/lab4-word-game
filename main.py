def update_game_state(secret_word, guessed_letters, guess, lives):
    low_guess = guess.lower()

    if low_guess in guessed_letters:
        return guessed_letters, lives

    new_guessed_letters = guessed_letters + [low_guess]

    if low_guess not in secret_word.lower():
        return new_guessed_letters, lives - 1

    return new_guessed_letters, lives


def get_display_word(secret_word, guessed_letters):
    display = [
        char if not char.isalpha() or char.lower() in guessed_letters 
        else "_" 
        for char in secret_word
    ]
    return " ".join(display)


def play_game(secret_word):
    """
    Play one round of hangman.
    
    Args:
        secret_word: The word the player needs to guess
        
    Returns:
        True if the player won, False if the player lost
    """
    lives = 6
    guessed_letters = []
    game_won = False
    
    while lives > 0 and not game_won:

        current_display = get_display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Lives remaining: {lives}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        guess = ""
        while not (len(guess) == 1 and guess.isalpha()):
            guess = input("Guess a letter: ").strip()
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid input. Please enter a single letter.")
        
        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)
        
        current_display = get_display_word(secret_word, guessed_letters)
        game_won = "_" not in current_display
    
    return game_won


def load_word():
    """
    Load a random word from words.txt.
    If the file is missing or empty, fall back to a hardcoded list.
    
    Returns:
        A random word as a string
    """
    import random
    
    fallback_words = ['epita', 'python', 'cybersecurity', 'quantum']
    
    try:
        with open('words.txt', 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        
        if words:
            return random.choice(words)
    except FileNotFoundError:
        pass
    
    return random.choice(fallback_words)


if __name__ == "__main__":
    print("Welcome to Hangman!")
    
    play_again = True
    while play_again:
        secret_word = load_word()
        won = play_game(secret_word)
        
        if won:
            print(f"\nCongratulations! You guessed it: {secret_word}")
        else:
            print(f"\nGame Over! The word was: {secret_word}")
        
        response = ""
        while response not in ['y', 'n']:
            response = input("\nPlay again? (y/n): ").strip().lower()
            if response not in ['y', 'n']:
                print("Please enter 'y' or 'n'.")
        play_again = (response == 'y')
    
    print("Thanks for playing!")
