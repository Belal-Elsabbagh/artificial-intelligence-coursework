import heapq

from labs.lab_4.structures.frontier_structure import Frontier


class PriorityQueue(Frontier):
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """

    def __init__(self):
        super().__init__()
        self.count = 0

    def push(self, item, priority=None):
        entry = (priority, item)
        heapq.heappush(self.list, entry)

    def pop(self):
        (priority, item) = heapq.heappop(self.list)
        return item

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, i) in enumerate(self.list):
            if i == item:
                if p <= priority:
                    break
                del self.list[index]
                self.list.append((priority, item))
                heapq.heapify(self.list)
                break
        else:
            self.push(item, priority)
