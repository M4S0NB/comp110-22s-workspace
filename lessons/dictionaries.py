"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26150

# print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from the dictionary
# By it's key
schools.pop("Duke")

# Test for existance of a key
is_duke_present: bool = "Duke" in schools

print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] = schools["NCSU"] + 200
print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26250}
print(schools)

# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")