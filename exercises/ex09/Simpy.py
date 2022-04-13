"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730481220"


class Simpy:
    """Class for statistical analysis."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values to our Simpy object."""
        self.values = values
    
    def __str__(self) -> str:
        """Returns a str representation of our list."""
        return f"Simpy({self.values})"

    def fill(self, value: float, number: int) -> None:
        """Fills out a Simpy with a specified number of a certain float."""
        i: int = number
        self.values: list[float] = []
        while i > 0:
            self.values.append(value)
            i -= 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates a list of floats in a range of floats with a specified step amount."""
        assert step != 0.0
        self.values: list[float] = []
        current: float = start
        if step > 0.0:
            while current < stop:
                self.values.append(current)
                current += step
        else:
            while current > stop:
                self.values.append(current)
                current += step
    
    def sum(self) -> float:
        """Sums up all the values in a Simpy."""
        total: float = 0.0
        for item in self.values:
            total += item
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overrides the add operater for Simpy class."""
        list: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                list.append(item + rhs)
            return Simpy(list)
        else:
            i: int = 0
            while i < len(self.values):
                list.append(self.values[i] + rhs.values[i])
                i += 1
            return Simpy(list)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overrides the exponentiation operater for Simpy class."""
        list: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                list.append(item ** rhs)
            return Simpy(list)
        else:
            i: int = 0
            while i < len(self.values):
                list.append(self.values[i] ** rhs.values[i])
                i += 1
            return Simpy(list)
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overrides the equal operator for Simpy class."""
        list: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                list.append(item == rhs)
            return list
        else:
            i: int = 0
            while i < len(self.values):
                list.append(self.values[i] == rhs.values[i])
                i += 1
            return list

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overrides the greater than operator for Simpy class."""
        list: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                list.append(item > rhs)
            return list
        else:
            i: int = 0
            while i < len(self.values):
                list.append(self.values[i] > rhs.values[i])
                i += 1
            return list
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overrides subscription notation for Simpy class."""
        list: list[float] = []
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    list.append(self.values[i])
                i += 1
            return Simpy(list)