class Frontier:
    def __init__(self):
        self.list = []

    def push(self, item, priority=None):
        self.list.append(item)

    def pop(self):
        return self.list.pop(0)

    def is_empty(self):
        return len(self.list) == 0
