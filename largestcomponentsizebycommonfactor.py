from collections import Counter

class Solution:
    def largestComponentSize(self, nums):

        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)

            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for num in nums:
            parent.setdefault(num, num)
            f = 2
            temp = num

            while f * f <= temp:
                if temp % f == 0:
                    union(num, f)
                    while temp % f == 0:
                        temp //= f
                f += 1

            if temp > 1:
                union(num, temp)

        count = Counter()

        for num in nums:
            root = find(num)
            count[root] += 1

        return max(count.values())