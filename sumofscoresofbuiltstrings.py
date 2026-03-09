def sumScores(self, s: str) -> int:
        
        n = len(s)
        Z = [0] * n
        
        left = right = 0
        
        for i in range(1, n):
            
            if i <= right:
                Z[i] = min(right - i + 1, Z[i - left])
            
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            
            if i + Z[i] - 1 > right:
                left = i
                right = i + Z[i] - 1
        
        return n + sum(Z)