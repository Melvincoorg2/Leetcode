def minSubarray(self, nums, p):

        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0

        prefix = 0
        min_len = len(nums)
        mod_map = {0: -1}   # important for subarray from start

        for i in range(len(nums)):

            prefix = (prefix + nums[i]) % p

            needed = (prefix - remainder) % p

            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            mod_map[prefix] = i

        if min_len == len(nums):
            return -1

        return min_len