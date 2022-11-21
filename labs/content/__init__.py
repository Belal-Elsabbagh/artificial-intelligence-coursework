"""
The given graph content.
"""

graph_dictionary: dict[str:dict[str:int]] = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'RimnicuVilcea': 80},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'RimnicuVilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Mehadia': {'Dobreta': 75, 'Lugoj': 70},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'RimnicuVilcea': 146},
    'Pitesti': {'Bucharest': 101, 'Craiova': 138, 'RimnicuVilcea': 97},
    'Fagaras': {'Bucharest': 211, 'Sibiu': 99},
    'Dobreta': {'Craiova': 120, 'Mehadia': 75},
    'Bucharest': {'Fagaras': 211, 'Giurgiu': 90, 'Pitesti': 101},
    'Giurgiu': {'Bucharest': 90}
}

short_graph_dictionary: dict[str:dict[str:int]] = {
    'A': {'S': 140, 'T': 118, 'Z': 75},
    'Z': {'A': 75, 'O': 71},
    'T': {'A': 118, 'L': 111},
    'S': {'A': 140, 'F': 99, 'O': 151, 'R': 80},
    'O': {'S': 151, 'Z': 71},
    'L': {'M': 70, 'T': 111},
    'R': {'C': 146, 'P': 97, 'S': 80},
    'M': {'D': 75, 'L': 70},
    'C': {'D': 120, 'P': 138, 'R': 146},
    'P': {'B': 101, 'C': 138, 'R': 97},
    'F': {'B': 211, 'S': 99},
    'D': {'C': 120, 'M': 75},
    'B': {'F': 211, 'G': 90, 'P': 101},
    'G': {'B': 90}
}

heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Fagaras': 178,
    'RimnicuVilcea': 193,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Dobreta': 242,
    'Pitesti': 98,
    'Craiova': 160,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Vaslui': 199,
    'Lasi': 226,
    'Neamt': 234,
    'Hirsova': 151,
    'Eforie': 161
}

exam_heuristic = {
    'A': 340,
    'Z': 350,
    'O': 380,
    'S': 215,
    'F': 210,
    'R': 146,
    'T': 310,
    'L': 200,
    'M': 170,
    'D': 120,
    'P': 138,
    'C': 190,
    'B': 0,
    'G': 150,
    'U': 280,
    'V': 450,
}

heuristic_costs = {
    'Arad': [['Zerind', 374], ['Timisoara', 329], ['Sibiu', 253]],
    'Zerind': [['Oradea', 380], ['Arad', 366]],
    'Oradea': [['Sibiu', 253]],
    'Sibiu': [['Rimniciu Vilcea', 193], ['Fagaras', 178], ['Arad', 366]],
    'Fagaras': [['Sibiu', 253], ['Bucharest', 0]],
    'Rimniciu Vilcea': [['Pitesti', 98], ['Craiova', 160], ['Sibiu', 253]],
    'Timisoara': [['Lugoj', 244], ['Arad', 366]],
    'Lugoj': [['Mehadia', 241]],
    'Mehadia': [['Lugoj', 244], ['Dorbeta', 242]],
    'Dobreta': [['Mehadia', 241], ['Craiova', 160]],
    'Pitesti': [['Craiova', 160], ['Bucharest', 0]],
    'Craiova': [['Pitesti', 98], ['Dobreta', 242], ['Rimniciu Vilcea', 193]],
    'Bucharest': [['Giurgiu', 77], ['Urziceni', 80], ['Fagaras', 178], ['Pitesti', 98]],
    'Giurgiu': [['Bucharest', 0]],
    'Urziceni': [['Vaslui', 199], ['Hirsova', 151], ['Bucharest', 0]],
    'Vaslui': [['Lasi', 226], ['Urziceni', 80]],
    'Lasi': [['Neamt', 234], ['Vaslui', 199]],
    'Neamt': [['Lasi', 226]],
    'Hirsova': [['Eforie', 161], ['Urziceni', 80]],
    'Eforie': [['Hirsova', 151]]
}
