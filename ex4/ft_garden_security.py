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
            print(f"Hight updated: {value}cm [OK]")
            return True
        elif value >= 0 and attribute == "age":
            print(f"Age updated: {value} days [OK]")
            return True
        elif attribute == "height":
            print(
                "Invalid operation attempted: "
                f"{attribute} {value}cm [REJECTED]"
            )
        elif attribute == "age":
            print(
                "Invalid operation attempted: "
                f"{attribute} {value} days [REJECTED]"
            )
        return False

    def set_height(self, height: int):
        if self._is_valid("height", height):
            self.height = height
        else:
            print("Security: Negative height rejected")


    def set_age(self, age: int):
        if self._is_valid("age", age):
            self.age = age
        else:
            print("Security: Impossible age rejected")

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

def ft_garden_security():
    pass


if __name__ == "__main__":
    ft_garden_security()

