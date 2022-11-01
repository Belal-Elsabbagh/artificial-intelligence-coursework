from labs.content import graph_dictionary, heuristic
from labs.lab_4.graph import Graph


def run():
    test_graph = Graph(graph_dictionary, heuristic)
    print(f'DFS result: {test_graph.search_dfs("Arad", "Bucharest")}')
    print(f'BFS result: {test_graph.search_bfs("Arad", "Bucharest")}')
    print(f'Uniform Cost Search result: {test_graph.search_ucs("Arad", "Bucharest")}')
    print(f'GBFS result: {test_graph.greedy_best_first_search("Arad", "Bucharest")}')
    print(f'A* result: {test_graph.a_star_search("Arad", "Bucharest")}')
