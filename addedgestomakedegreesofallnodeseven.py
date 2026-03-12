class Solution:
 def isPossible(self, n: int, edges: List[List[int]]) -> bool:
    degree = [0] * (n + 1)
    edge_set = set()

    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
        edge_set.add((min(a, b), max(a, b)))

    odd = [i for i in range(1, n + 1) if degree[i] % 2 == 1]

    def has_edge(a, b):
        return (min(a, b), max(a, b)) in edge_set

    if len(odd) == 0:
        return True

    if len(odd) == 2:
        a, b = odd
        # connect them directly
        if not has_edge(a, b):
            return True
        # route through a third node c
        for c in range(1, n + 1):
            if c != a and c != b:
                if not has_edge(a, c) and not has_edge(b, c):
                    return True
        return False

    if len(odd) == 4:
        a, b, c, d = odd
        # 3 ways to pair 4 nodes into 2 edges
        # (a-b, c-d), (a-c, b-d), (a-d, b-c)
        if not has_edge(a, b) and not has_edge(c, d):
            return True
        if not has_edge(a, c) and not has_edge(b, d):
            return True
        if not has_edge(a, d) and not has_edge(b, c):
            return True
        return False

    return False
