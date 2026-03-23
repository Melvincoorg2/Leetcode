class Solution:
 def findTargetSumWays(self, nums: List[int], target: int) -> int:

    dp = {0: 1}  # {current_sum: ways}

    for num in nums:
        next_dp = {}
        for s, count in dp.items():
            next_dp[s + num] = next_dp.get(s + num, 0) + count
            next_dp[s - num] = next_dp.get(s - num, 0) + count
        dp = next_dp

    return dp.get(target, 0)   