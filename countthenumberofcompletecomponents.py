class Solution:
 def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    for a, b in edges:
        union(a, b)

    # count nodes and edges per component
    node_count = {}
    edge_count = {}

    for i in range(n):
        root = find(i)
        node_count[root] = node_count.get(root, 0) + 1

    for a, b in edges:
        root = find(a)
        edge_count[root] = edge_count.get(root, 0) + 1

    result = 0
    for root in node_count:
        k = node_count[root]
        e = edge_count.get(root, 0)
        if e == k * (k - 1) // 2:
            result += 1

    return result
