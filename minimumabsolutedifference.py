def minimumAbsDifference(self, arr):

        arr.sort()

        min_diff = float('inf')
        result = []

        # Step 1: find minimum difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            min_diff = min(min_diff, diff)

        # Step 2: collect pairs
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result