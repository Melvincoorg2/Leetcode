class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        res = [-1, -1]
        res_len = float("inf")

        left = 0

        for right in range(len(s)):

            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            # shrink window
            while have == need_count:

                # update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # remove from left
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""