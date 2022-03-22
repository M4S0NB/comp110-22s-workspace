def vowels_and_threes(string: str) -> str:
    string2: str = ""
    i: int = 0
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    while i < len(string):
        if (i % 3 == 0) and (not string[i] in vowels):
            string2 += string[i]
        elif (string[i] in vowels) and (not i % 3 == 0):
            string2 += string[i]
        i += 1
    return string2
    

print(vowels_and_threes("comp110"))


def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
    averages: dict[str, float] = dict()
    total_grade: int = 0
    for person in grades:
        total_grade = 0
        i: int = 0
        while i < len(grades[person]):
            total_grade += grades[person][i]
            i += 1
        average: float = total_grade / len(grades[person])
        averages[person] = average
    return averages


print(average_grades({'bill': [75, 94, 97], 'annie': [88, 93, 99]}))


def grocery_list(inventory: dict[str, int], buy: dict[str, int]) -> list[str]:
    bought: list[str] = list()
    for item in buy:
        if item in inventory and inventory[item] >= buy[item]:
            bought.append(item)
    return bought


print(grocery_list({"milk": 3, "bread": 2, "chips": 1}, {"milk": 2, "bread": 1, "salsa": 1, "chips": 1}))


def ends_with(words: list[str], character: str) -> list[str]:
    new_words: list[str] = list()
    i: int = 0
    while i < len(words):
        current_word = words[i]
        if current_word[len(current_word) - 1] == character:
            new_words.append(words[i])
        i += 1
    return new_words


print(ends_with(["banana", "eartha", "manga"], "a"))