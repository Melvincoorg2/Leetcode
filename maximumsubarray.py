class Solution:
 def maxSubArray(self, nums: List[int]) -> int:

    cur = result = nums[0]
    for num in nums[1:]:
        cur = max(num, cur + num)
        result = max(result, cur)
    return result