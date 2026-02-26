def licenseKeyFormatting(self, s: str, k: int) -> str:

        # Step 1: remove dashes and convert to uppercase
        cleaned = ""
        for ch in s:
            if ch != '-':
                cleaned += ch.upper()

        result = ""
        count = 0

        # Step 2: build from the end
        for i in range(len(cleaned) - 1, -1, -1):

            result = cleaned[i] + result
            count += 1

            if count == k and i != 0:
                result = "-" + result
                count = 0

        return result