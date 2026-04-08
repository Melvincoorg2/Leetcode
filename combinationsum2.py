class Solution:
 def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

    candidates.sort()
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            # skip duplicates at same level
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])  # i+1 → no reuse
            path.pop()

    backtrack(0, [], target)
    return result