class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def fencing_cost(self, price_per_meter):
        return self.perimeter() * price_per_meter


if __name__ == "__main__":
    rectangles = [
        Rectangle(3, 5),
        Rectangle(10, 20),
        Rectangle(1, 1),
        Rectangle(7, 2),
        Rectangle(4, 8),
    ]

    for rect in rectangles:
        print(rect.area())