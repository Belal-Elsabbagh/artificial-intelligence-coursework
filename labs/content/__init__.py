"""
The given graph content.
"""

graph_dictionary: dict[str:dict[str:int]] = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'RimnicuVilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'RimnicuVilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Craiova': {'Dobreta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138},
    'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90}
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
