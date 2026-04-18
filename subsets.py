class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            res.append(path[:])   # store current subset

            for i in range(start, len(nums)):
                path.append(nums[i])          # choose
                backtrack(i + 1, path)        # explore
                path.pop()                    # undo

        backtrack(0, [])
        return res