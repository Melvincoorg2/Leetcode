class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n - 1
        length = 0

        # Step 1: Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Step 2: Count characters of last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
