def findKthBit(self, n: int, k: int) -> str:
        
        if n == 1:
            return "0"
        
        mid = 1 << (n - 1)  # 2^(n-1)
        
        if k == mid:
            return "1"
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        # mirrored position
        val = self.findKthBit(n - 1, (1 << n) - k)
        
        return "1" if val == "0" else "0"