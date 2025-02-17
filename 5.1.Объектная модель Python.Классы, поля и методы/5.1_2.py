class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, distance):
        return round(((self.x - distance.x) ** 2 + (self.y - distance.y) ** 2) ** 0.5, 2)
