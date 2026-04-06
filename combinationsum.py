class Solution:
 def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                continue
            path.append(c)
            backtrack(i, path, remaining - c)  # i not i+1 → reuse allowed
            path.pop()

    backtrack(0, [], target)
    return result