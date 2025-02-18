class Rectangle:
    def __init__(self, corner_one: tuple[float, float], corner_two: tuple[float, float]):
        self.x1, self.y1 = corner_one
        self.x2, self.y2 = corner_two
        self.width = round(abs(self.x1 - self.x2), 2)
        self.height = round(abs(self.y1 - self.y2), 2)

    def get_pos(self):
        return (round(min(self.x1, self.x2), 2), round(max(self.y1, self.y2), 2))

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_size(self):
        return (self.width, self.height)

    def move(self, x, y):
        self.x1 += x
        self.x2 += x
        self.y1 += y
        self.y2 += y

    def resize(self, width, height):
        self.width = width
        self.height = height
        if self.x1 > self.x2:
            self.x1 = self.width + self.x2
        else:
            self.x2 = self.width + self.x1
        if self.y1 > self.y2:
            self.y2 = self.y1 - self.height
        else:
            self.y1 = self.y2 - self.height
