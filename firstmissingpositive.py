def firstMissingPositive(self, nums):

        n = len(nums)

        # Step 1: Place numbers in correct positions
        for i in range(n):

            while (1 <= nums[i] <= n and
                   nums[nums[i] - 1] != nums[i]):

                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Step 2: Find first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1