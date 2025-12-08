class Plant:
    """Represents a plant with attributes."""

    def __init__(self, name: str, height: int, age_days: int):
        """Initialize a plant with name, height and age (in days)."""
        self.name = name
        self.height = height
        self.age_days = age_days

    def get_info(self):
        """Display plant information."""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self):
        """Increase plant height by 1cm."""
        self.height += 1

    def age(self):
        """Increase plant age by 1 day."""
        self.age_days += 1


def ft_plant_growth():
    """Simulate plant growth over a week for multiple plants."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    growing_plants = [rose, sunflower, cactus]
    for plant in growing_plants:
        day = 1
        initial_height = plant.height
        print(f"=== Day {day} ===")
        plant.get_info()

        while day < 7:
            plant.grow()
            plant.age()
            day += 1

        print(f"=== Day {day} ===")
        plant.get_info()
        growth = plant.height - initial_height
        print(f"Growth this week: +{growth}cm\n")


if __name__ == "__main__":
    ft_plant_growth()
