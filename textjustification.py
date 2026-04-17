class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_words = []
            length = 0

            # Step 1: pick words
            while i < n and length + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                length += len(words[i])
                i += 1

            # Step 2: format line
            spaces = maxWidth - length
            gaps = len(line_words) - 1

            # last line OR single word
            if i == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))

            else:
                space_per_gap = spaces // gaps
                extra = spaces % gaps

                line = ""
                for j in range(gaps):
                    line += line_words[j]
                    line += " " * (space_per_gap + (1 if j < extra else 0))

                line += line_words[-1]

            res.append(line)

        return res