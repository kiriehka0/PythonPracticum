class Queue:
    def __init__(self):
        self.queue0 = []

    def push(self, item):
        self.queue0.append(item)

    def is_empty(self):
        if len(self.queue0) == 0:
            return True
        else:
            return False

    def pop(self):
        self.one_element = self.queue0[0]
        self.queue0 = self.queue0[1:]
        return self.one_element
