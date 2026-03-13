class Solution:
 def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    for u, v in edges:
        union(u, v)

    return find(source) == find(destination)