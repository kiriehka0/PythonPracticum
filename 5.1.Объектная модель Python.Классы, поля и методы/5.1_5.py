class Rectangle:
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    def __init__(self, *args):
        self.x1 = args[0][0]
        self.y1 = args[0][1]
        self.x2 = args[1][0]
        self.y2 = args[1][1]

    def perimeter(self):
        return round(2 * abs(self.x2 - self.x1) + 2 * abs(self.y2 - self.y1), 2)

    def area(self):
        return round(abs(self.x1 - self.x2) * abs(self.y1 - self.y2), 2)
