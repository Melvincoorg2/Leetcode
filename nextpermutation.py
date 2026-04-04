class Solution:
 def nextPermutation(self, nums: List[int]) -> None:

    n = len(nums)
    i = n - 2

    # find first decreasing element from right
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        # find smallest element greater than nums[i] from right
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # reverse the suffix
    nums[i+1:] = nums[i+1:][::-1]