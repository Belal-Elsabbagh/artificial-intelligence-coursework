import codecs
import json

from labs.content import short_graph_dictionary
from labs.lab_4.graph import Graph
from labs.lab_4.problem import Problem
from labs.lab_4.search import *


def run():
    test_problem = Problem(short_graph_dictionary, "A", "B")
    result = {
        'dfs': dfs(test_problem),
        'bfs': bfs(test_problem),
        'ucs': ucs(test_problem),
        'gbfs': greedy_best_first_search(test_problem, graph_heuristic),
        'a*': a_star_search(test_problem, graph_heuristic)
    }
    with open("out/graph_search_results/sample.json", "w") as outfile:
        outfile.write(json.dumps(result, indent=4))
