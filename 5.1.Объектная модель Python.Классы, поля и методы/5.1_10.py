class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.a = self.stack[-1]
        self.stack = self.stack[:-1]
        return self.a

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
