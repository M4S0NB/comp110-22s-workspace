"""One shot wordle game."""

__author__ = "730481220"

secret_word: str = "python"

length_of_word: int = len(secret_word)

guess: str = input(f"What is your {length_of_word}-letter guess? ")

while len(guess) != len(secret_word):
    print(f"that was not {length_of_word} letters! Try again: ")
    guess: str = input(f"What is your {length_of_word}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0

i2:int = 0
# i2 is the index in the secret word only, and is used to see if character i is located in another index

resulting_emojis = ""

while i < len(guess):
    # loop for determining colors of squares
    character_in_word: bool = False
    i2 = 0
    if guess[i] == secret_word[i]:
        resulting_emojis += f"{GREEN_BOX}"
        character_in_word = True
    else:
        while (i2 < len(guess) and not character_in_word):
            # loop to check each letter of secret word to find if there should be yellow squares
            if guess[i] == secret_word[i2]:
                resulting_emojis += f"{YELLOW_BOX}"
                character_in_word: bool = True
            i2 += 1
        if not character_in_word:
            resulting_emojis += f"{WHITE_BOX}"
    i += 1

print(resulting_emojis)
    
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")