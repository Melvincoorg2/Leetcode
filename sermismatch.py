def findErrorNums(self, nums):

        duplicate = -1
        missing = -1

        # Step 1: Find duplicate
        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] *= -1

        # Step 2: Find missing
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]