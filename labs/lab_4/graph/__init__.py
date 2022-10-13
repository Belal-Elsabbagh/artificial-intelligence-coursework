"""
A Graph class that supports multiple searching algorithms.
"""
from labs.lab_4.priority_queue import PriorityQueue


class Graph:
    """
    The graph class is a wrapper class for the graph dictionary.
    """
    __adjacency_list: dict[str:dict[str:int]] = None

    def __init__(self, adjacency_list):
        self.__adjacency_list: dict[str:dict[str:int]] = adjacency_list

    def get_adjacency_list(self) -> dict[str:dict[str:int]]:
        return self.__adjacency_list

    def get_number_of_nodes(self):
        return len(self.get_adjacency_list().keys())

    def __dfs_search_util(self, node, goal, visited_list: list[str] = None):
        if visited_list is None:
            visited_list = list()
        visited_list.append(node)
        if visited_list[-1] is goal:
            return True
        for neighbour in self.get_adjacency_list()[node]:
            if neighbour not in visited_list:
                res = self.__dfs_search_util(neighbour, goal, visited_list)
                if res:
                    return visited_list

    def __dfs_util(self, node, visited_list = None):
        if visited_list is None:
            visited_list = list()
        visited_list.append(node)
        for neighbour in self.get_adjacency_list()[node]:
            if neighbour not in visited_list:
                self.__dfs_util(neighbour, visited_list)
        return visited_list

    def get_dfs_sequence(self, start_node) -> list[str]:
        return self.__dfs_util(start_node)

    def get_node_dfs(self,start, goal):
        return self.__dfs_search_util(start, goal)

    def search_bfs(self, start_node, search_node) -> list[str] | None:
        node = start_node
        queue = [node]
        visited: dict[str:bool] = {node: True}
        while search_node not in visited:
            node = queue.pop(0)
            for i in self.get_adjacency_list()[node]:
                if i not in visited:
                    queue.append(i)
                    visited[i] = True
        return list(visited.keys())

    def get_bfs_sequence(self, start_node) -> list[str] | None:
        node = start_node
        queue = [node]
        visited: dict[str:bool] = {node: True}
        while queue:
            node = queue.pop(0)
            for i in self.get_adjacency_list()[node]:
                if i not in visited:
                    queue.append(i)
                    visited[i] = True
        return list(visited.keys())

    def uniform_cost_search(self, start):
        node = start
        queue = PriorityQueue()
        visited: dict[str:bool] = {node: True}
        while queue.queue:
            node = queue.delete()
            neighbors = self.get_adjacency_list()[node]
            for i in neighbors:
                if i not in visited:
                    queue.insert(i)
                    visited[i] = True
        return list(visited.keys())
