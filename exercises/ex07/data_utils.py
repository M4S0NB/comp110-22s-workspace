"""Dictionary related utility functions."""

__author__ = "730481220"

# Define your functions below

from csv import DictReader


def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    """Read rows of a csv into a 'table'."""
    result: list[dict[str, str]] = list()

    # Open a handle to the data fiile
    file_handle = open(file_name, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    
    # Read each row of CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = list()
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = dict()

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(original_dict: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Returns a new dictionary with only the first N rows of the dictionary."""
    new_dict: dict[str, list[str]] = {}

    if N > len(original_dict):
        return original_dict
    for column in original_dict:
        i: int = 0
        first_n_values: list[str] = []
        while i < N:
            first_n_values.append(original_dict[column][i])
            i += 1
        new_dict[column] = first_n_values

    return new_dict


def select(original_table: dict[str, list[str]], needed_columns: list[str]) -> dict[str, list[str]]:
    """Includes only a the necesary columns in a table."""
    new_table: dict[str, list[str]] = {}

    for column in original_table:
        if column in needed_columns:
            new_table[column] = (original_table[column])

    return new_table


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combined two column oriented tables."""
    new_table: dict[str, list[str]] = {}

    for column in first_table:
        new_table[column] = first_table[column]

    for column in second_table:
        if column in new_table:
            i: int = 0
            while i < len(second_table[column]):
                new_table[column].append(second_table[column][i])
                i += 1
        else:
            new_table[column] = second_table[column]

    return new_table


def count(list: list[str]) -> dict[str, int]:
    """Counts items in a list and stores them in a dictionary."""
    counts: dict[str, int] = {}
    for item in list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts