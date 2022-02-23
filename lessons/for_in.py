"""An example of for in syntax."""

names: list[str] = ["Mason", "Ashley", "Scott", "Rachel"]

# Example of iterating through names using a while loop
print("While output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for..in output:")
# Doing the same thing with a for in loop
for name in names:
    print(name)