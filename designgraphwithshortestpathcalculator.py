import heapq
from collections import defaultdict

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = defaultdict(list)
        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf')] * self.n
        dist[node1] = 0
        heap = [(0, node1)]

        while heap:
            cost, node = heapq.heappop(heap)
            if cost > dist[node]:
                continue
            if node == node2:
                return cost
            for neighbor, weight in self.adj[node]:
                new_cost = cost + weight
                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))

        return -1 if dist[node2] == float('inf') else dist[node2]
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)