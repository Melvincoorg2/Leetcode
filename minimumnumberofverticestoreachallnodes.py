class Solution:
 def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

    in_degree = [0] * n
    
    for src, dst in edges:
        in_degree[dst] += 1
    
    result = []
    for i in range(n):
        if in_degree[i] == 0:
            result.append(i)
    
    return result

