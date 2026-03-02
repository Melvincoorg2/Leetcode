def waysToMakeFair(self, nums):

        n = len(nums)

        total_even = 0
        total_odd = 0

        for i in range(n):
            if i % 2 == 0:
                total_even += nums[i]
            else:
                total_odd += nums[i]

        left_even = 0
        left_odd = 0
        count = 0

        for i in range(n):

            if i % 2 == 0:
                right_even = total_even - left_even - nums[i]
                right_odd = total_odd - left_odd
            else:
                right_even = total_even - left_even
                right_odd = total_odd - left_odd - nums[i]

            new_even = left_even + right_odd
            new_odd = left_odd + right_even

            if new_even == new_odd:
                count += 1

            # update prefix
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]

        return count