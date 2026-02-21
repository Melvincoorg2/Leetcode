def findDisappearedNumbers(self, nums):

        # Step 1: Mark numbers
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1

        # Step 2: Collect missing numbers
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result