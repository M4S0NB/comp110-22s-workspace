"""Examples of default parameters."""


def add(x: int, y: int = 0) -> int:
    """Default parameters give more flexibility."""
    # Default parameters must follow required parameters
    return x + y


print(add(1))