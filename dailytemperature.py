def dailyTemperatures(self, temperatures):

        n = len(temperatures)
        answer = [0] * n
        stack = []  # store indices

        for i in range(n):

            # While current temp is warmer than stack top temp
            while stack and temperatures[i] > temperatures[stack[-1]]:

                prev_index = stack.pop()
                answer[prev_index] = i - prev_index

            stack.append(i)

        return answer