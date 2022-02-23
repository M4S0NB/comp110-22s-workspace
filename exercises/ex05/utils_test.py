"""File for testing utils."""

__author__ = "730481220"


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_none_even() -> None:
    assert only_evens([1, 3, 5]) == []


def test_only_evens_empty() -> None:
    assert only_evens([]) == []


def test_only_evens_many() -> None:
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_sub_none() -> None:
    assert sub([], 1, 3) == []


def test_sub_end_too_small() -> None:
    assert sub([1, 2, 3], -2, -1) == []


def test_sub_end_too_big() -> None:
    assert sub([1, 2, 3, 4], 1, 6) == [2, 3, 4]


def test_sub_start_negative() -> None:
    assert sub([1, 2, 3, 4], -1, 2) == [1, 2]


def test_sub_many() -> None:
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_concat_empty() -> None:
    assert concat([], []) == []


def test_concat_single() -> None:
    assert concat([1], []) == [1]


def test_concat_many() -> None:
    assert concat([1, 2], [3, 4, 5]) == [1, 2, 3, 4, 5]