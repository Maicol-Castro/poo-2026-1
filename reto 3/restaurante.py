class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_price(self) -> float:
        return self.price


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, is_shareable: bool):
        super().__init__(name, price)
        self.is_shareable = is_shareable


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, calories: int):
        super().__init__(name, price)
        self.calories = calories


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self) -> float:
        total = sum(item.calculate_price() for item in self.items)

        # descuento simple: si hay más de 3 items → 10%
        if len(self.items) >= 3:
            total *= 0.9

        return total


if __name__ == "__main__":
    order = Order()

    order.add_item(Beverage("Coke", 5.0, "Medium"))
    order.add_item(Appetizer("Nachos", 8.0, True))
    order.add_item(MainCourse("Burger", 15.0, 800))

    print("Total:", order.calculate_total())