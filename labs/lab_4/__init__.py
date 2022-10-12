import labs.lab_4.content
from labs.lab_4.graph import Graph


def run_lab_4():
    test_graph = Graph(content.graph_dictionary)

    print(f'DFS result: {test_graph.get_dfs_sequence("Arad", "Lugoj")}')
    print(f'BFS result: {test_graph.get_bfs_sequence("Arad", "Lugoj")}')
    print(f'Uniform Cost Search result: {test_graph.uniform_cost_search("Arad", "Lugoj")}')