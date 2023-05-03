"""
    DSatur algorithm from: https://en.wikipedia.org/wiki/DSatur
"""

import collections

def max_dsat (neighbor_colors, graph):
    """
        Returns the vertex with the highest degree of saturation,
        using the highest degree to break ties.
        Parameters:
            neighbor_colors : dict - A dictionary with a vertex as a key and a set of its
                    neighbors colors
            graph : dict - A graph represented as an adjacency list

    """
    max_val = -1
    max_vertex = None
    for v in graph:
        if len (neighbor_colors[v]) > max_val or (len (neighbor_colors[v]) == max_val and len (graph[v]) > len (graph[max_vertex])):
            max_val = len (neighbor_colors[v])
            max_vertex = v
    return max_vertex


def dsatur (graph, neighbor_colors):
    """
        Implements the DSatur algorithm (greedy) for approximating the min coloring of a graph
        Parameters:
            graph : dict - An subgraph of the graph to be colored represented as an adjacency list,
                    each key is an uncolored vertex in the graph
            neighbor_colors : dict - A dictionary where the keys are vertices and the values
                    are the set of colors in the neighborhood
    """
    colorings = {}
    while (len (graph) > 0):
        u = max_dsat (neighbor_colors, graph)
        i = 0
        while u not in colorings:
            if i not in neighbor_colors[u]:
                colorings[u] = i
            i += 1
        neighbors = graph.pop (u)
        for v in neighbors:
            neighbor_colors[v].add (colorings[u])
    return colorings

def main ():
    n = int (input ())
    graph = {}
    uncolored_graph = {}
    neighbor_colors = {}
    for _ in range (n):
        u, v = input ().split ()
        if u not in graph:
            graph[u] = set ()
            uncolored_graph[u] = set ()
        if v not in graph:
            graph[v] = set ()
            uncolored_graph[v] = set ()
        graph[u].add (v)
        graph[v].add (u)
        uncolored_graph[u].add (v)
        uncolored_graph[v].add (u)
        neighbor_colors[u] = set ()
        neighbor_colors[v] = set ()
    
    colorings = dsatur (uncolored_graph, neighbor_colors)

    print (max (colorings.values ()))
    sorted_colorings = collections.OrderedDict (sorted (colorings.items ()))
    for v in sorted_colorings:
        print (v + " " + str (colorings[v]))



if __name__ == "__main__":
    main ()
