"""Utility functions for csv analysis."""

__author__ = "730481220"


from csv import DictReader


def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    """Read rows of a csv into a 'table'."""
    result: list[dict[str, str]] = list()

    # Open a handle to the data file
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


def count(list: list[str]) -> dict[str, int]:
    """Counts items in a list and stores them in a dictionary."""
    counts: dict[str, int] = {}
    for item in list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def average_number(numbers: list[float]) -> float:
    """Returns the average number in a list of floats."""
    total: float = 0.0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average


def experience_quantified_as_numbers(amounts_of_experience: list[str]) -> list[float]:
    """Specifically for exercise 8, returns a list that quantifies amount of experience as a single number of months."""
    list_of_months: list[float] = []
    for row in amounts_of_experience:
        if row == "None to less than one month!":
            list_of_months.append(0.0)
        elif row == "2-6 months":
            list_of_months.append(4.0)
        elif row == "7-12 months":
            list_of_months.append(9.0)
        elif row == "1-2 years":
            list_of_months.append(18.0)
        elif row == "Over 2 years":
            list_of_months.append(24.0)
    return list_of_months