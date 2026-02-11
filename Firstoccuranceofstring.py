class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # If needle is bigger, impossible
        if m > n:
            return -1

        # Try every starting index
        for i in range(n - m + 1):
            j = 0

            # Compare characters
            while j < m and haystack[i + j] == needle[j]:
                j += 1

            # If we matched full needle
            if j == m:
                return i

        return -1
