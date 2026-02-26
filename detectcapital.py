def detectCapitalUse(self, word: str) -> bool:

        uppercase_count = 0

        for ch in word:
            if 'A' <= ch <= 'Z':
                uppercase_count += 1

        # Case 1: all uppercase
        if uppercase_count == len(word):
            return True

        # Case 2: all lowercase
        if uppercase_count == 0:
            return True

        # Case 3: only first letter uppercase
        if uppercase_count == 1 and 'A' <= word[0] <= 'Z':
            return True

        return False