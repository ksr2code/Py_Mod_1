class Plant:
    """Represents a plant with attributes."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with name, height and age (in days)."""
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        """Display plant information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
    """Manage data and display information of multiple plants."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.display_info()
    sunflower.display_info()
    cactus.display_info()


if __name__ == "__main__":
    ft_garden_data()
