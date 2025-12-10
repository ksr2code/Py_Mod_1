class Plant:
    """Base plant."""

    def __init__(self, name: str, height: int):
        """Initialize a plant with name, height and age (in days)."""
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    """Plant that can flower."""
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """Flowering plant with prize points."""
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

class GardenManager:
    """Manages multiple gardens with analytics."""

    total_gardens = 0  # Class variable

    class GardenStats:
        """Nested helper class for statistics."""
        # Calculate stats here

    def __init__(self, owner):
        """Instance method - create garden for owner."""
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant):
        """Instance method - add plant to this garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        """Instance method - grow all plants."""
        pass

    def generate_report(self):
        """Instance method - use GardenStats to show analytics."""
        pass

    @classmethod
    def create_garden_network(cls):
        """Class method - works on GardenManager class."""
        pass

    @staticmethod
    def validate_height(height):
        """Static method - utility function."""
        pass


