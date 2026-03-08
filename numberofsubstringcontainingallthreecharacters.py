def numberOfSubstrings(self, s: str) -> int:
        
        last = [-1, -1, -1]  # positions of a,b,c
        result = 0
        
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
            result += min(last) + 1
            
        return result