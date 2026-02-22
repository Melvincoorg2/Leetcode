from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:

            fn_id, status, time = log.split(":")
            fn_id = int(fn_id)
            time = int(time)

            if status == "start":

                if stack:
                    # Add time to currently running function
                    result[stack[-1]] += time - prev_time

                stack.append(fn_id)
                prev_time = time

            else:  # "end"

                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result
