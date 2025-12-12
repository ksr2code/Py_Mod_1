class Plant:
    """Base plant."""

    def __init__(self, name: str, height: int):
        """Initialize a plant with name and height."""
        self.name = name
        self.height = height

    def get_info(self):
        """Display plant information."""
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Plant that can flower."""

    def __init__(self, name: str, height: int, color: str):
        """Initialize a flowering plant with name, height and color."""
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        """Display flowering plant information."""
        print(f"- {self.name}: {self.height}cm"
              f", {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """Flowering plant with prize points."""

    def __init__(self, name: str, height: int, color: str, prize_points: int):
        """Initialize a prize flower plant with parent and own attributes"""
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        """Display prize flower information."""
        print(f"- {self.name}: {self.height}cm"
              f", {self.color} flowers (blooming)"
              f", Prize points: {self.prize_points}")


class GardenManager:
    """Manages multiple gardens with analytics."""

    total_gardens = 0
    all_gardens = {}

    class GardenStats:
        """Nested helper class for statistics."""

        def __init__(self):
            """Initialize statistics tracking."""
            self.total_plants = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_plants = 0
            self.total_height = 0
            self.total_prize_points = 0

        def calculate_score(self) -> int:
            """Calculate garden score from metrics."""
            score = self.total_height + self.total_prize_points
            score += self.total_growth * 10
            return score

    def __init__(self, owner: str):
        """Instance method - create garden for owner."""
        self.owner = owner
        self.plants = {}
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1
        GardenManager.all_gardens[self.owner] = self

    def add_plant(self, plant: Plant):
        """Instance method - add plant to this garden."""
        self.plants[plant.name] = plant
        self.stats.total_plants += 1
        self.stats.total_height += plant.height

        if plant.__class__.__name__ == "PrizeFlower":
            self.stats.prize_plants += 1
            self.stats.total_prize_points += plant.prize_points  # type: ignore
        elif plant.__class__.__name__ == "FloweringPlant":
            self.stats.flowering_plants += 1
        elif plant.__class__.__name__ == "Plant":
            self.stats.regular_plants += 1

        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        """Instance method - grow all plants."""
        print(f"{self.owner} is helping all plants to grow...")
        for k in self.plants:
            self.plants[k].height += 1
            print(f"{k} grew 1cm")
            self.stats.total_growth += 1
            self.stats.total_height += 1

    def generate_report(self):
        """Instance method - use GardenStats to show analytics."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for k in self.plants:
            self.plants[k].get_info()
        print()
        print(f"Plants added: {self.stats.total_plants}, "
              f"Total growth: {self.stats.total_growth}")
        print(f"Plant types: {self.stats.regular_plants} regular, "
              f"{self.stats.flowering_plants} flowering, "
              f"{self.stats.prize_plants} prize flowers")
        print()

    @classmethod
    def create_garden_network(cls, owners: list):
        """Class method - create multiple gardens."""
        gardens = {}
        for owner in owners:
            gardens[owner] = cls(owner)
        return gardens

    @classmethod
    def display_network(cls):
        """Class method - display network statistics."""
        print(f"Height validation test: "
              f"{cls.validate_height(cls.all_gardens)}")

        scores = "Garden scores - "
        first = True
        for k in cls.all_gardens:
            if not first:
                scores += ", "
            scores += f"{k}: {cls.all_gardens[k].stats.calculate_score()}"
            first = False
        print(scores)
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(gardens: dict) -> bool:
        """Static method - validate all plants have positive heights."""
        for g in gardens:
            for k in gardens[g].plants:
                if gardens[g].plants[k].height < 0:
                    return False
        return True


def ft_garden_analytics():
    """Demonstrate garden management system."""
    print("=== Garden Management System Demo ===\n")

    # Create gardens using class method
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = gardens["Alice"]
    bob = gardens["Bob"]

    # Add plants to Alice's garden
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()

    # Add plants to Bob's garden
    bob.add_plant(Plant("Cactus", 40))
    bob.add_plant(FloweringPlant("Tulip", 30, "pink"))
    print()

    # Grow all plants
    alice.grow_all()
    print()
    bob.grow_all()
    print()

    # Generate reports
    alice.generate_report()
    bob.generate_report()

    # Display network statistics
    GardenManager.display_network()


if __name__ == "__main__":
    ft_garden_analytics()
