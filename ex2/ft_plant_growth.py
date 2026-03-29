class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = float(height)
        self.age = age
        self.growth = growth

    def __str__(self):
        return f"{self.name}: {round(self.height, 1)}cm, {self.age} days old"

    def grow(self):
        self.height += self.growth
        self.age += 1

    def get_info(self):
        return str(self)


def main():
    rose = Plant("Rose", 25, 30, .8)
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        print(rose.get_info())
        rose.grow()
    print(f"Growth this week: {round(rose.growth * 7)}cm")


if __name__ == "__main__":
    main()
