"""Full Wordle game using functions to organize information."""

__author__ = "730481220"


def contains_char(secret_word: str, character_guess: str) -> bool:
    """Function that determines if the character is found in secret word."""
    assert len(character_guess) == 1
    i = 0

    # loop that returns true if character is found in the secret word
    while i < len(secret_word):
        if secret_word[i] == character_guess:
            return True
        i += 1

    return False


# These are the named constants for the different emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(word_guess: str, secret_word: str) -> str:
    """Emojis representing correctness of guessed word."""
    assert len(word_guess) == len(secret_word)
    resulting_emojis: str = ""
    i: int = 0

    # loop that creates the string of emojis
    while len(resulting_emojis) < len(secret_word):
        if word_guess[i] == secret_word[i]:
            resulting_emojis += f"{GREEN_BOX}"
        # makes use of the contains_char function to decide if the character is in there somewhere
        elif contains_char(secret_word, word_guess[i]):
            resulting_emojis += f"{YELLOW_BOX}"
        else:
            resulting_emojis += f"{WHITE_BOX}"
        i += 1

    return resulting_emojis


def input_guess(expected_length: int) -> str:
    """Prompts the user to give a correct length guess."""
    word_guess: str = input(f"Enter a {expected_length} character word: ")

    while len(word_guess) != expected_length:
        print(f"that was not {expected_length} chars! Try again: ")
        word_guess = input()

    return word_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    won_game: bool = False
    secret_word: str = "codes"
    out_of_turns: bool = False

    while (not won_game) and (not out_of_turns):
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turn_number}/6 turns!")
            won_game = True
        if turn_number > 5:
            out_of_turns = True
        turn_number += 1

    if not won_game:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()  