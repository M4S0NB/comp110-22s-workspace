"""Functions using Dictionaries."""

__author__ = "730481220"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = dict()
    for key in original_dict:
        if original_dict[key] in new_dict:
            raise KeyError("Duplicate key in the new dictionary!")
        new_dict[original_dict[key]] = key
    return new_dict


print(invert({'kris': 'jordan', 'bruh': 'moment'}))


def count(original_list: list[str]) -> dict[str, int]:
    new_dictionary: dict[str, int] = dict()
    for item in original_list:
        if item in new_dictionary:
            new_dictionary[item] += 1
        else:
            new_dictionary[item] = 1
    return new_dictionary


def favorite_color(peoples_favorite_colors: dict[str, str]) -> str:
    colors_list: list = list()
    for item in peoples_favorite_colors:
        colors_list.append(peoples_favorite_colors[item])
    color_counts: dict[str, int] = count(colors_list)
    favorite: str = colors_list[0]
    for color in color_counts:
        if color_counts[color] > color_counts[favorite]:
            favorite = color
    return favorite


print(favorite_color({"mason": "yellow", "ashley": "yellow", "maddie": "yellow", "dean": "blue", "rikki": "blue"}))