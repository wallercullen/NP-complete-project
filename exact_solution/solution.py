from itertools import permutations


def verify_k_coloring(k, coloring, edges):
   if k != len(set(coloring.values())):
       return False
   for v1, v2 in edges:
       if coloring[v1] == coloring[v2]:
           return False
   return True


def colorings(graph):
   for permutation in permutations(graph.keys()):  # O(V!)
       coloring = dict([(v, -1) for v in permutation])
       for v in permutation:  # O(V)
           for color in range(len(coloring)):  # O(V)
               adjacent_colors = map(coloring.__getitem__, graph[v])  # O(V)
               if color not in adjacent_colors:  # O(1)
                   coloring[v] = color
                   break
       yield coloring


def min_coloring(graph):
   return min(colorings(graph), key=lambda c: max(c.values()))  # O(V^2)

def main():
    N = int(input())

    graph = dict()

    for _ in range(N):
        u, v = input().split()
        if u not in graph:
            graph[u] = set()
        graph[u].add(v)
        if v not in graph:
            graph[v] = set()
        graph[v].add(u)

    coloring = min_coloring(graph)

    # O(n)
    print(len(set(coloring.values())))

    # O(n)
    for v, color in coloring.items():
        print(v, color)


if __name__ == "__main__":
    main()
