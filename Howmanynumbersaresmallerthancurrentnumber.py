def smallerNumbersThanCurrent(self, nums):

        # Step 1: Count frequency
        freq = [0] * 101

        for num in nums:
            freq[num] += 1

        # Step 2: Build prefix sum
        for i in range(1, 101):
            freq[i] += freq[i - 1]

        # Step 3: Build answer
        result = []

        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(freq[num - 1])

        return result