"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional


__author__ = "730481220"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Gives value in a list at a certain index."""
    if head is None:
        raise ValueError("value_at cannot be called with None")
    elif index == 0:
        return head.data
    elif head.next is None and index != 0:
        raise IndexError("Index is out of bounds on the list.")
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Gives the maximum value in a list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:
        return head.data
    elif head.next.data < head.data:
        head.next.data = head.data
    return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:
    """Turns a list into a linked list of Nodes."""
    if items is None:
        return None
    if len(items) > 0:
        head: Node = Node(items[0], linkify(items[1:]))
        return head


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Multiplies values in a list by a factor."""
    if head is None:
        return None
    else:
        new: Node = Node(head.data * 2, scale(head.next, factor))
    return new


print(linkify([1]))
print(Node(1, Node(2, Node(3, None))))