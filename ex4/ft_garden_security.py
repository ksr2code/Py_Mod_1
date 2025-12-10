class Plant:
    """Represents a plant with attributes."""

    def __init__(self, name: str):
        """Initialize a plant with name, height and age (in days)."""
        self.name = name
        self.height = 0
        self.age = 0
        print(f"Plant created: {self.name}")

    def get_info(self):
        """Display plant information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def _is_valid(self, attribute: str, value: int) -> bool:
        """Validate the attribute is not negative"""
        if value >= 0 and attribute == "height":
            return True
        elif value >= 0 and attribute == "age":
            return True
        elif attribute == "height":
            print(
                "\nInvalid operation attempted: "
                f"{attribute} {value}cm [REJECTED]"
            )
        elif attribute == "age":
            print(
                "\nInvalid operation attempted: "
                f"{attribute} {value} days [REJECTED]"
            )
        return False

    def set_height(self, height: int):
        """Set plant height if value is valid."""
        if self._is_valid("height", height):
            self.height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print("Security: Negative height rejected\n")

    def set_age(self, age: int):
        """Set plant age if value is valid."""
        if self._is_valid("age", age):
            self.age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Security: Impossible age rejected\n")

    def get_height(self) -> int:
        """Get plant height."""
        return self.height

    def get_age(self) -> int:
        """Get plant age."""
        return self.age


def ft_garden_security():
    """Demonstrate plant security system with validation."""
    print("=== Garden Security System ===")
    rose = Plant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-1)
    print(f"Current plant: {rose.name} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
