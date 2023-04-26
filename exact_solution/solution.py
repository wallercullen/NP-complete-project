from itertools import permutations


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

colorings = []
# O(n! n^3)
for perm in permutations(graph.keys()):  # O(n!)
    # O(n)
    coloring = dict([(v, -1) for v in perm])    # O(n)
    # O(n^3)
    for v in perm:                              # O(n)
        for x in range(0, len(coloring)):               # O(n)
            if x not in map(coloring.__getitem__, graph[v]):    # O(n)
                coloring[v] = x
                break
    colorings.append(coloring)                  # O(1)

# O(n! n)
min_coloring = min(colorings, key=lambda coloring: sum(
    coloring.values()))

# O(n)
print(len(set(min_coloring.values())))

# O(n)
for v, color in min_coloring.items():
    print(v, color)
