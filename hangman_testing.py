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


def test_update_game_state():
    # Setup initial state
    word = "python"
    
    # Test 1: A correct new guess
    letters, lives = update_game_state(word, [], "p", 6)
    assert "p" in letters
    assert lives == 6
    print("Test 1 Passed: Correct guess handled.")

    # Test 2: An incorrect new guess
    letters, lives = update_game_state(word, ["p"], "z", 6)
    assert "z" in letters
    assert lives == 5
    print("Test 2 Passed: Incorrect guess deducted life.")

    # Test 3: A duplicate guess (should not change anything)
    letters, lives = update_game_state(word, ["p"], "p", 6)
    assert letters == ["p"]
    assert lives == 6
    print("Test 3 Passed: Duplicate guess ignored.")

    # Test 4: Case sensitivity
    letters, lives = update_game_state(word, [], "Y", 6)
    assert "y" in letters
    assert lives == 6
    print("Test 4 Passed: Case sensitivity handled.")

if __name__ == "__main__":
    try:
        test_update_game_state()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\nA test failed!")