from labs.lab_4.structures.frontier_structure import Frontier


class Stack(Frontier):
    """A container with a last-in-first-out (LIFO) queuing policy."""

    def __init__(self):
        super().__init__()

    def push(self, item, priority=None):
        """Push 'item' onto the stack"""
        self.list.append(item)

    def pop(self):
        return self.list.pop()

