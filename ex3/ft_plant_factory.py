class Plant:
    """Represents a plant with attributes."""

    total_plants = 0

    def __init__(self, name: str, starting_height: int, starting_age: int):
        """Initialize a plant with name, height and age (in days)."""
        self.name = name
        self.height = starting_height
        self.age = starting_age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")
        Plant.total_plants += 1


def ft_plant_factory():
    """Create and intialize multiple plants."""
    print("=== Plant Factory Output ===")
    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)
    print(f"Total Plants created: {Plant.total_plants}")


if __name__ == "__main__":
    ft_plant_factory()
