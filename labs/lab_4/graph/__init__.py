"""
A Graph class that supports multiple searching algorithms.
"""
import json
from datetime import datetime

from labs.lab_4.structures.priority_queue import PriorityQueue


class Graph:
    """
    The graph class is a wrapper class for the graph dictionary.
    """
    __adjacency_list: dict[str:dict[str:int]] = None

    def __init__(self, adjacency_list, heuristic_costs_list):
        self.__adjacency_list: dict[str:dict[str:int]] = adjacency_list
        self.__heuristic_costs_list = heuristic_costs_list

    def get_adjacency_list(self) -> dict[str:dict[str:int]]:
        return self.__adjacency_list

    def get_number_of_nodes(self):
        return len(self.get_adjacency_list().keys())

    def get_neighbors(self, node):
        return self.get_adjacency_list()[node]

    def get_heuristic_cost_of_node(self, node, neighbor, priority):
        return self.__heuristic_costs_list[node]

    def get_cost_of_edge(self, start, end):
        return self.get_adjacency_list().get(start).get(end)

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

    def __dfs_util(self, node, visited_list=None):
        if visited_list is None:
            visited_list = list()
        self.visit_node(node, visited_list)
        for neighbour in self.get_neighbors(node):
            if neighbour not in visited_list:
                self.__dfs_util(neighbour, visited_list)
        return visited_list

    def get_dfs_sequence(self, start_node) -> list[str]:
        return self.__dfs_util(start_node)

    def search_dfs(self, start, goal):
        return self.__dfs_search_util(start, goal)

    def search_bfs(self, start_node, search_node) -> list[str] | None:
        node = start_node
        queue = [node]
        visited: dict[str:bool] = {node: True}
        while search_node not in visited:
            node = queue.pop(0)
            visited[node] = True
            for i in self.get_neighbors(node):
                if i not in visited:
                    queue.append(i)
        return list(visited.keys()) if search_node in visited.keys() else None

    def get_bfs_sequence(self, start_node) -> list[str] | None:
        node = start_node
        queue = [node]
        visited: dict[str:bool] = {}
        while queue:
            node = queue.pop(0)
            visited[node] = True
            for i in self.get_neighbors(node):
                if i not in visited:
                    queue.append(i)
        return list(visited.keys())

    def __search_by_priority(self, _start, _goal, calculate_priority):
        node = _start
        visited: dict[str:bool] = {}
        path = [node]
        priority = calculate_priority(node, path, 0)
        open_list = PriorityQueue()
        open_list.push(path, priority)
        while not open_list.is_empty():
            node, path, priority = self.get_front_node(open_list)
            self.visit_node(node, visited)
            if node == _goal:
                result = {
                    'path': path,
                    'cost': self.get_cost_of_path(path),
                    'visited_order': list(visited.keys())
                }
                now = datetime.now()
                json_result = json.dumps(result, indent=4)
                return result
            neighbors = self.get_neighbors(node)
            for neighbor, cost in neighbors.items():
                if neighbor in visited:
                    continue
                path_to_neighbor = path + [neighbor]
                open_list.update(path_to_neighbor, calculate_priority(neighbor, path_to_neighbor, priority))

    def greedy_best_first_search(self, _start, _goal):
        return self.__search_by_priority(_start, _goal, self.get_heuristic_cost_of_node)

    def a_star_search(self, _start, _goal):
        return self.__search_by_priority(_start, _goal, self.get_expected_cost)

    def search_ucs(self, _start, _goal):
        return self.__search_by_priority(_start, _goal, self.get_ucs_priority)

    def get_ucs_priority(self, node, path, priority):
        return self.get_cost_of_path(path)

    def get_expected_cost(self, node, path, priority):
        return self.get_cost_of_path(path) + self.get_heuristic_cost_of_node(node, path, priority)

    @staticmethod
    def visit_node(node, visited_list):
        visited_list[node] = True

    @staticmethod
    def get_front_node(open_list):
        path, priority = open_list.pop()
        node = path[-1]
        return node, path, priority

    @staticmethod
    def node_is_in_open_list(neighbor, open_list):
        return neighbor not in (i[2][0] for i in open_list.heap)

    def get_cost_of_path(self, path):
        return sum([self.get_cost_of_edge(previous, current) for previous, current in zip(path, path[1:])])
