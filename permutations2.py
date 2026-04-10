class Solution:
 def permuteUnique(self, nums: List[int]) -> List[List[int]]:

    nums.sort()
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        seen = set()
        for i in range(len(remaining)):
            if remaining[i] in seen:
                continue
            seen.add(remaining[i])
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()

    backtrack([], nums)
    return result