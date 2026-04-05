class Solution:
 def findSubstring(self, s: str, words: List[str]) -> List[int]:

    if not s or not words:
        return []

    w_len = len(words[0])
    w_count = len(words)
    total = w_len * w_count
    word_freq = Counter(words)
    result = []

    for start in range(w_len):  # w_len independent windows
        left = start
        curr = Counter()
        matched = 0

        for right in range(start, len(s) - w_len + 1, w_len):
            word = s[right: right + w_len]

            if word in word_freq:
                curr[word] += 1
                if curr[word] <= word_freq[word]:
                    matched += 1

                # shrink window if over-counted
                while curr[word] > word_freq[word]:
                    left_word = s[left: left + w_len]
                    curr[left_word] -= 1
                    if curr[left_word] < word_freq[left_word]:
                        matched -= 1
                    left += w_len

                if matched == w_count:
                    result.append(left)
                    # slide left pointer forward
                    left_word = s[left: left + w_len]
                    curr[left_word] -= 1
                    if curr[left_word] < word_freq[left_word]:
                        matched -= 1
                    left += w_len
            else:
                # invalid word, reset window
                curr.clear()
                matched = 0
                left = right + w_len

    return result