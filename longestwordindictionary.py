class Solution:
 def longestWord(self, words: List[str]) -> str:

    word_set = set(words)
    result = ""

    for word in words:
        if all(word[:i] in word_set for i in range(1, len(word))):
            if len(word) > len(result) or (len(word) == len(result) and word < result):
                result = word

    return result