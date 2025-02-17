class RedButton:

    def __init__(self, x=0):
        self.x = x

    def click(self):
        print("Тревога!")
        self.x += 1

    def count(self):
        return self.x
