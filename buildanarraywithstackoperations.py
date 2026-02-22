def buildArray(self, target, n):

        result = []
        current = 1
        i = 0

        while i < len(target):

            if current < target[i]:
                result.append("Push")
                result.append("Pop")
                current += 1

            else:
                result.append("Push")
                current += 1
                i += 1

        return result