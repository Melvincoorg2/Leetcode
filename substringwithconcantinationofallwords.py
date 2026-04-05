class Solution:
 def findSubstring(self, s: str, words: List[str]) -> List[int]:

    if not s or not words:
        return []

    w_len = len(words[0])
    w_count = len(words)
    total = w_len * w_count
    word_freq = Counter(words)
    result = []

    for i in range(len(s) - total + 1):
        seen = Counter()
        j = 0
        while j < w_count:
            word = s[i + j * w_len: i + (j+1) * w_len]
            if word not in word_freq:
                break
            seen[word] += 1
            if seen[word] > word_freq[word]:
                break
            j += 1
        if j == w_count:
            result.append(i)

    return result