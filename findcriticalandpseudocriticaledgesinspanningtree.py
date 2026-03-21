class Solution:
 def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        

    # preserve original indices
    indexed = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
    indexed.sort()

    def make_uf():
        parent = list(range(n))
        rank = [0] * n
        return parent, rank

    def find(parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(parent, rank, a, b):
        a, b = find(parent, a), find(parent, b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True

    def kruskal(skip=-1, force=-1):
        parent, rank = make_uf()
        weight = 0
        count = 0
        # force an edge first
        if force != -1:
            w, u, v, _ = indexed[force]
            union(parent, rank, u, v)
            weight += w
            count += 1
        for idx, (w, u, v, i) in enumerate(indexed):
            if idx == skip:
                continue
            if union(parent, rank, u, v):
                weight += w
                count += 1
        return weight if count == n - 1 else float('inf')

    base = kruskal()
    critical = []
    pseudo = []

    for i in range(len(indexed)):
        # critical: removing raises cost
        if kruskal(skip=i) > base:
            critical.append(indexed[i][3])
        # pseudo: forcing in still achieves base cost
        elif kruskal(force=i) == base:
            pseudo.append(indexed[i][3])

    return [critical, pseudo]
