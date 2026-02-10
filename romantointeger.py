def value(ch):
     if ch == 'I': 
        return 1
     if ch == 'V': 
        return 5
     if ch == 'X': 
        return 10
     if ch == 'L': 
        return 50
     if ch == 'C': 
        return 100
     if ch == 'D': 
        return 500
     if ch == 'M': 
        return 1000
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            curr = value(s[i])

            if i + 1 < n:
                next_val = value(s[i + 1])
                if curr < next_val:
                    total -= curr
                else:
                    total += curr
            else:
                total += curr

        return total


     

        