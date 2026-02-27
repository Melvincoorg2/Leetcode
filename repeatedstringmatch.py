def repeatedStringMatch(self, a: str, b: str) -> int:

        temp = ""
        count = 0

        # Repeat until temp length >= b length
        while len(temp) < len(b):
            temp += a
            count += 1

        if b in temp:
            return count

        # One extra repetition for overlap case
        temp += a
        count += 1

        if b in temp:
            return count

        return -1