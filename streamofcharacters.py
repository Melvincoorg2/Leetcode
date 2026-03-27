class StreamChecker:

    def __init__(self, words: list[str]):
        # build trie of reversed words
        self.trie = {}
        for word in words:
            node = self.trie
            for ch in reversed(word):
                node = node.setdefault(ch, {})
            node['#'] = True

        self.max_len = max(len(w) for w in words)
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        node = self.trie
        # walk stream backwards, traverse trie
        for ch in reversed(self.stream[-self.max_len:]):
            if ch not in node:
                return False
            node = node[ch]
            if '#' in node:
                return True

        return False