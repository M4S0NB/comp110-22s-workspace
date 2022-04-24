"""Tests for linked list utils."""
import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730481220"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_non_empty() -> None:
    """Gives you the data value at a certain index in the list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_value_at_out_of_bounds() -> None:
    """If the index is too high, it will result in a Index error."""
    linked_list = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 3)


def test_max_word_in_middle() -> None:
    """Should return the highest value."""
    linked_list = Node(1, Node(7, Node(3, None)))
    assert max(linked_list) == 7


def test_max_empty() -> None:
    """Should raise ValueError when given empty list."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify_empty() -> None:
    """Should return None for empty list."""
    assert linkify([]) is None


def test_linkify_non_empty() -> None:
    """The list should be changed into a list of linked Nodes."""
    assert print(linkify([1, 2, 3])) == print(Node(1, Node(2, Node(3, None))))


def test_scale_empty() -> None:
    """None should be returned when using scale on an empty list."""
    assert scale(None, 2) is None


def test_scale_non_empty() -> None:
    """Should multiply all the values of the list by 2."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert print(scale(linked_list, 2)) == print(Node(2, Node(4, Node(6, None))))