"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute definitions
    size: str = "small"
    toppings: int = 0
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float:
        """Calculate price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        
        total += self.toppings * .75

        if self.extra_cheese:
            total += 1.0
        
        total += tax

        return total


a_pizza: Pizza = Pizza("large", 3)
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(a_pizza)
print(a_pizza.size)
print(Pizza)
print(f"Price: {a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
print(a_pizza.size)
print(Pizza("small", 2).price(100))