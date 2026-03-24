class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self):
        self.height += self.growth
        self.age += 1

    def get_info(self):
        return str(self)


def main():
    rose = Plant("Rose", 25, 30, 1)
    print("=== Day 1 ===")
    print(rose.get_info())
    for i in range(6):
        rose.grow()
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: + {rose.growth * 6}")


if __name__ == "__main__":
    main()
