class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        k -= 1  # convert to 0-based

        result = []
        fact = math.factorial(n-1)

        for i in range(n, 0, -1):

            index = k // fact
            result.append(nums[index])
            nums.pop(index)

            if i > 1:
                k %= fact
                fact //= (i-1)

        return "".join(result)