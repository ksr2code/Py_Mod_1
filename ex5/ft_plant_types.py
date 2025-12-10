class Plant:
    """Represents a base class."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with name, height and age (in days)."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """Display plant information."""
        print(
            f"{self.name} ({self.__class__.__name__}) "
            f"{self.height}cm, {self.age} days"
        )


class Flower(Plant):
    """Represents Flower subclass of Plant class."""

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Display blooming message."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        """Display flower information."""
        print(
            f"{self.name} ({self.__class__.__name__}) "
            f"{self.height}cm, {self.age} days"
            f", {self.color} color"
        )


class Tree(Plant):
    """Represents Tree subclass of Plant class."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Calculate and display shade area."""
        shade_area = int(((self.trunk_diameter / 100) * 10) ** 2 * 3.14)
        print(f"{self.name} provides {shade_area} square meters of shade")

    def get_info(self):
        """Display tree information."""
        print(
            f"{self.name} ({self.__class__.__name__}) "
            f"{self.height}cm, {self.age} days"
            f", {self.trunk_diameter} cm diameter"
        )


class Vegetable(Plant):
    """Represents Vegetable subclass of Plant class."""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_nutrition(self):
        """Display nutritional information."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        """Display vegetable information."""
        print(
            f"{self.name} ({self.__class__.__name__}) "
            f"{self.height}cm, {self.age} days"
            f", {self.harvest_season} harvest"
        )


def ft_plant_types():
    """Demonstrate specialized plant types with inheritance."""
    # Create 2 flowers
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 40, 45, "yellow")

    # Create 2 trees
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 800, 3650, 75)

    # Create 2 vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 120, "autumn", "beta-carotene")

    print("=== Garden Plant Types ===\n")

    # Display flowers
    rose.get_info()
    rose.bloom()
    print()

    tulip.get_info()
    tulip.bloom()
    print()

    # Display trees
    oak.get_info()
    oak.produce_shade()
    print()

    pine.get_info()
    pine.produce_shade()
    print()

    # Display vegetables
    tomato.get_info()
    tomato.display_nutrition()
    print()

    carrot.get_info()
    carrot.display_nutrition()


if __name__ == "__main__":
    ft_plant_types()
