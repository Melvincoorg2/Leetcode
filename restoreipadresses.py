def restoreIpAddresses(self, s: str):

        result = []

        def backtrack(start, path):

            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for length in range(1, 4):

                if start + length > len(s):
                    break

                segment = s[start:start+length]

                if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                    continue

                path.append(segment)
                backtrack(start + length, path)
                path.pop()

        backtrack(0, [])
        return result