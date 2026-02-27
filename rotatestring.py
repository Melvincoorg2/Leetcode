def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        temp = s

        for _ in range(len(s)):
            if temp == goal:
                return True

            temp = temp[1:] + temp[0]

        return False