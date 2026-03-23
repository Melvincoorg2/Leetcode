class Solution:
 def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

    MOD = 10**9 + 7

    def kadane(a):
        max_sum = cur = 0
        for x in a:
            cur = max(0, cur + x)
            max_sum = max(max_sum, cur)
        return max_sum

    total = sum(arr)

    if k == 1:
        return kadane(arr) % MOD

    two_copy = kadane(arr * 2)

    if total > 0:
        result = two_copy + (k - 2) * total
    else:
        result = two_copy

    return result % MOD