class Solution:
 def canJump(self, nums: List[int]) -> bool:

    farthest = 0
    for i, n in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + n)
    return True