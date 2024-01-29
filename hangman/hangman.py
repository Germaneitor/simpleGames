# hangman.py

from random import choice
import string

MAX_INCORRECT_GUESSES = 6

def select_word():
    """
    Get words from a file to utilize in the game.
    """
    # Words can be added to this file
    with open("hangwords.txt") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

def get_player_input(guessed_letters):
    """
    Player's turn loop.
    """
    while True:
        player_input = input("Guess a letter: ").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input

def _validate_input(player_input, guessed_letters):
    """
    Makes sure that exactly one character (letter) was input
    by the user, that it is an alphabetical letter and that it
    has not been already guessed by player.
    """
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )

def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))

def build_guessed_word(target_word, guessed_letters):
    """
    This function will create the guessed word so far.
    If no correct letter is guessed, a dash will fill that
    space; otherwise, correctly guessed letter are added to
    the string.
    """
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)

def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])

def game_over(wrong_guesses, target_word, guessed_letters):
    """
    Checked if all letters have been guessed correctly or
    wrong guesses have been reached (6 guesses total).
    """
    return (
        wrong_guesses == MAX_INCORRECT_GUESSES
        or set(target_word) <= guessed_letters
    )

def finished_game(wrong_guesses, target_word):
    """
    Make the check to see if word has been guessed or if the max
    amount of available guesses has been met to finish the game.
    """
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lost!")
    else:
        print("Congrats! You did it!")
    print(f"Your word was: {target_word}")

def main_game(wrong_guesses, target_word, guessed_letters, guessed_word):
    """
    Main game loop that will iterate for each player's turn until either
    the player guesses the word correctly or reaches the limit of guesses.
    It will also utilize the different functions to check wheter their input
    is a valid guess or not.
    """
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is: {guessed_word}")
        print(
            "Current guessed letters: "
            f"{join_guessed_letters(guessed_letters)}\n"
        )

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1
        
        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    # Game over
    finished_game(wrong_guesses, target_word)

if __name__ == "__main__":
    # Initial setup
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print("Welcome to Hangman!")

    # Game loop
    main_game(wrong_guesses, target_word, guessed_letters, guessed_word)