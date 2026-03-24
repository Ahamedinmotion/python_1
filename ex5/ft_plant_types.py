class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.age} days"

    def special_action(self):
        pass


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def __str__(self):
        base = super().__str__()
        return f"{base}, {self.color} color (Flower)"

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def special_action(self):
        self.bloom()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def __str__(self):
        base = super().__str__()
        return f"{base}, {self.trunk_diameter}cm trunk diameter (Tree)"

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def special_action(self):
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self):
        base = super().__str__()
        return f"{base}, {self.harvest_season} harvest (Vegetable)"

    def nutrition_info(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def special_action(self):
        self.nutrition_info()


def main():
    print("=== Garden Plant Types ===")
    plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 600, 2000, 40),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "spring", "beta-carotene"),
    ]
    for plant in plants:
        print(plant)
    print()
    for plant in plants:
        plant.special_action()


if __name__ == "__main__":
    main()
