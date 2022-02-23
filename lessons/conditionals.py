"""An example of conditional (if-else) statements."""

SECRET = 3

print("Im thinking of a number between 1 and 5, what is it?")

guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("Well done!, ")
else:
    print("Better luck next time")
    if guess > SECRET:
        print("try guessing lower")
    else:
        print("Try guessing higher")

print("Thanks for playing!")