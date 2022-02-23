"""File for testing utils."""

__author__ = "730481220"


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_none_even() -> None:
    """Only evens test for when none in the list are even."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_empty() -> None:
    """Only evens test for when the list is empty."""
    assert only_evens([]) == []


def test_only_evens_many() -> None:
    """Only evens test for when there are many even numbers in the list."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_sub_none() -> None:
    """Sub test for when the list is empty."""
    assert sub([], 1, 3) == []


def test_sub_end_too_small() -> None:
    """Sub test for when the end is less than 0."""
    assert sub([1, 2, 3], -2, -1) == []


def test_sub_end_too_big() -> None:
    """Sub test for when the end is larger than the length of list."""
    assert sub([1, 2, 3, 4], 1, 6) == [2, 3, 4]


def test_sub_start_negative() -> None:
    """Sub test for when the start is a negative number."""
    assert sub([1, 2, 3, 4], -1, 2) == [1, 2]


def test_sub_many() -> None:
    """Sub test for a normal list with a range of multiple numbers."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_concat_empty() -> None:
    """Concat test for when the lists are empty."""
    assert concat([], []) == []


def test_concat_single() -> None:
    """Concat test for when one list is empty."""
    assert concat([1], []) == [1]


def test_concat_many() -> None:
    """Concat test for when both lists have many values."""
    assert concat([1, 2], [3, 4, 5]) == [1, 2, 3, 4, 5]