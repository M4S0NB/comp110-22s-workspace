"""Examples of using lists in a simple 'game'."""


from random import randint


rolls: list[int] = list() 

last_index: int = len(rolls) - 1


while len(rolls) == 0 or rolls[last_index] != 1:
    rolls.append(randint(1, 6))
print(rolls)
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls!
i: int = 0
sum: int = 0

while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"Total score: {sum}")