def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}   # dictionary: number -> index

    for i in range(len(nums)):
        current = nums[i]
        needed = target - current

        # check if required number is already seen
        if needed in seen:
            return [seen[needed], i]

        # store current number with its index
        seen[current] = i
