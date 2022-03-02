"""File for testing out my dictionary functions."""

import pytest
from dictionary import invert
from dictionary import count
from dictionary import favorite_color


def test_invert_empty() -> None:
    """Test for inverting an empty dictionary."""
    assert invert({}) == {}


def test_invert_normal() -> None:
    """Test for inverting a normal dictionary with multiple keys and values."""
    assert invert({"bruh": "moment", "mason": "boyles", "comp": "110"}) == {"moment": "bruh", "boyles": "mason", "110": "comp"}


def test_invert_key_error() -> None:
    """Test to make sure the invert function raises a keyerror when there are duplicate keys."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_count_empty() -> None:
    """Tests that the count function works with an empty list."""
    assert count([]) == {}


def test_count_normal() -> None:
    """Test for how the count function works in a normal implication with several entries."""
    assert count(["blue", "blue", "yellow", "red", "blue"]) == {"blue": 3, "yellow": 1, "red": 1}


def test_count_single() -> None:
    """Testing the count function for a single entry."""
    assert count(["blue"]) == {"blue": 1}


def test_favorite_color_tie() -> None:
    """Testing for what happens when two colors are tied."""
    assert favorite_color({"mason": "blue", "ashley": "pink"}) == "blue"


def test_favorite_color_normal() -> None:
    """Testing for how the favorite color function wors in a normal situation with multiple entries."""
    assert favorite_color({"mason": "blue", "ashley": "pink", "dean": "blue", "ian": "pink", "nick": "blue"}) == "blue"


def test_favorite_color_single() -> None:
    """Testing for what happens when there is only one key-value pair."""
    assert favorite_color({"mason": "blue"}) == "blue"
