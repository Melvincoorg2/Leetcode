class Solution:
 def countAndSay(self, n: int) -> str:

    s = "1"
    for _ in range(n - 1):
        next_s = ""
        i = 0
        while i < len(s):
            ch = s[i]
            count = 0
            while i < len(s) and s[i] == ch:
                count += 1
                i += 1
            next_s += str(count) + ch
        s = next_s
    return s