class Problem:
    __graph: dict[str:dict[str:int]] = None

    def __init__(self, graph, start, goal):
        self.__graph = graph
        self.__start = start
        self.__goal = goal

    def get_start_state(self):
        return self.__start

    def is_goal_state(self, state):
        return state == self.__get_goal_state()

    def __get_goal_state(self):
        return self.__goal

    def get_successors(self, state):
        return self.__graph[state]

    def __get_cost_of_edge(self, start, end):
        return self.__graph.get(start).get(end)

    def get_cost_of_path(self, path):
        return sum([self.__get_cost_of_edge(previous, current) for previous, current in zip(path, path[1:])])
