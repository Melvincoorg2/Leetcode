
class Solution:
 def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

    fwd = defaultdict(list)
    rev = defaultdict(list)

    for u, v, w in edges:
        fwd[u].append((v, w))
        rev[v].append((u, w))

    def dijkstra(graph, src):
        dist = [float('inf')] * n
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            cost, node = heapq.heappop(heap)
            if cost > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))
        return dist

    d1   = dijkstra(fwd, src1)   # src1 -> all nodes
    d2   = dijkstra(fwd, src2)   # src2 -> all nodes
    ddst = dijkstra(rev, dest)   # all nodes -> dest

    result = float('inf')
    for m in range(n):
        if d1[m] < float('inf') and d2[m] < float('inf') and ddst[m] < float('inf'):
            result = min(result, d1[m] + d2[m] + ddst[m])

    return result if result < float('inf') else -1