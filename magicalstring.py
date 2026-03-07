def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1

        s = [1,2,2]
        i = 2
        num = 1

        while len(s) < n:
            for _ in range(s[i]):
                s.append(num)
            num = 3 - num  # switch between 1 and 2
            i += 1

        return s[:n].count(1)