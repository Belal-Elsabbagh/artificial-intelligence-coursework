import json

from labs.content import exam_heuristic
from labs.lab_4.structures.priority_queue import PriorityQueue
from labs.lab_4.structures.queue import Queue
from labs.lab_4.structures.stack import Stack


def graph_heuristic(state, problem=None):
    return exam_heuristic[state]


def no_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def calculate_priority(blind_search, heuristic_fn, ignore_cost, new_path, next_node, problem):
    cost_of_path = problem.get_cost_of_path(new_path) if not ignore_cost else 0
    return (cost_of_path + heuristic_fn(next_node, problem)) if not blind_search else None


def init_search_engine(_problem, blind_search):
    visited_list = []
    path = []
    start_position = _problem.get_start_state()
    path = [start_position]
    priority = None if blind_search else 0
    return path, priority, start_position, visited_list


def push_to_frontier(frontier, _object, priority=None):
    if priority is None:
        frontier.push(_object)
        return
    frontier.update(_object, priority)


def search_engine(_problem, _open_list, ignore_cost=False, blind_search=False, heuristic_fn=no_heuristic):
    """Runs a search on the given problem with the given data structure to store the frontiers."""
    path, priority, position, visited_list = init_search_engine(_problem, blind_search)
    push_to_frontier(_open_list, (position, path), priority)
    solution = {
        'visited': [],
        'frontier': []
    }
    while not _open_list.is_empty():
        position, path = _open_list.pop()
        if position in visited_list:
            continue
        visited_list.append(position)
        if _problem.is_goal_state(position):
            return {
                'path': path,
                'cost': _problem.get_cost_of_path(path),
                'visited': visited_list,
                'solution': solution
            }
        successors = _problem.get_successors(position)
        for next_node, _ in successors.items():
            if next_node in visited_list:
                continue
            new_path = path + [next_node]
            new_priority = calculate_priority(blind_search, heuristic_fn, ignore_cost, new_path, next_node, _problem)
            push_to_frontier(_open_list, (next_node, new_path), new_priority)
        solution['visited'].append(list(visited_list))
        solution['frontier'].append(list(_open_list.list))


def dfs(problem):
    """Search the deepest nodes in the search tree first."""
    return search_engine(problem, Stack(), ignore_cost=True, blind_search=True)


def bfs(problem):
    """Search the shallowest nodes in the search tree first."""
    return search_engine(problem, Queue(), ignore_cost=True, blind_search=True)


def ucs(problem):
    """Search the node of the least total cost first."""
    return search_engine(_problem=problem, _open_list=PriorityQueue(), ignore_cost=False, blind_search=False)


def a_star_search(problem, heuristic_fn=no_heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    return search_engine(_problem=problem, _open_list=PriorityQueue(), heuristic_fn=heuristic_fn)


def greedy_best_first_search(problem, heuristic_fn=no_heuristic):
    """Search the node that has the lowest heuristic first."""
    return search_engine(_problem=problem, _open_list=PriorityQueue(), ignore_cost=True, heuristic_fn=heuristic_fn)
