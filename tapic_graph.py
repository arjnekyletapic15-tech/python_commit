"""Assessment 3.3: Non-Linear Data Structure
Undirected Graph built from the last name TAPIC.

Vertices: T, A, P, I, C
Edges   : T-A, T-P, A-I, A-C, P-C

    T --- A --- I
    |     |
    P --- C
"""
from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        self.adj.setdefault(v, [])

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        """Breadth-First Search using a queue."""
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            v = queue.popleft()
            order.append(v)
            for n in self.adj[v]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return order

    def dfs(self, start):
        """Depth-First Search using a stack."""
        visited = set()
        stack = [start]
        order = []
        while stack:
            v = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            order.append(v)
            # reversed so neighbors are visited in listed order
            for n in reversed(self.adj[v]):
                if n not in visited:
                    stack.append(n)
        return order


if __name__ == "__main__":
    g = Graph()
    for u, v in [("T", "A"), ("T", "P"), ("A", "I"), ("A", "C"), ("P", "C")]:
        g.add_edge(u, v)

    print("Graph for TAPIC")
    for v, neighbors in g.adj.items():
        print(f"  {v}: {neighbors}")
    print("BFS from T:", " -> ".join(g.bfs("T")))
    print("DFS from T:", " -> ".join(g.dfs("T")))