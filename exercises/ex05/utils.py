"""Exercise 5."""

__author__ = "730481220"


def only_evens(integers: list[int]) -> list[int]:
    """Takes a list of ints and returns the even ones."""
    even_numbers: list[int] = []
    for number in integers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def sub(numbers: list[int], start: int, end: int) -> list[int]:
    """Takes a list of ints and returns indexes from a given start to end."""
    sub_list: list[int] = []
    i: int = start
    if start > len(numbers) or end <= 0 or end < start:
        return sub_list
    if i < 0:
        i = 0
    while i < end and i < len(numbers):
        sub_list.append(numbers[i])
        i += 1
    return sub_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Combines two lists of ints."""
    new_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        new_list.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        new_list.append(list_2[i])
        i += 1
    return new_list