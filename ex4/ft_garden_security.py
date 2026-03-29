class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0.0
        self._age = 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = float(height)
        print(f"Height updated: {height}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def __str__(self):
        return f"{self.name}: {self._height:.1f}cm, {self._age} days old"


def main():
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15, 10)
    print(f"Plant created: {plant}")

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-2)

    print(f"Current state: {plant}")


if __name__ == "__main__":
    main()
