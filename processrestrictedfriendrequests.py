class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            # union by rank
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
        
        result = []
        
        for u, v in requests:
            pu, pv = find(u), find(v)
            
            # Check if merging pu and pv violates any restriction
            violated = False
            for x, y in restrictions:
                px, py = find(x), find(y)
                # After merging pu+pv, would x and y end up in the same component?
                if (px == pu or px == pv) and (py == pu or py == pv):
                    violated = True
                    break
            
            if violated:
                result.append(False)
            else:
                union(u, v)
                result.append(True)
        
        return result