def getHappyString(self, n: int, k: int) -> str:
        
        result = []
        
        def backtrack(s):
            
            if len(s) == n:
                result.append(s)
                return
            
            for ch in "abc":
                if not s or s[-1] != ch:
                    backtrack(s + ch)
        
        backtrack("")
        
        if k <= len(result):
            return result[k-1]
        return ""