class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.key_val  = {}
        self.key_freq = {}
        self.freq_keys = defaultdict(OrderedDict)

    def _increment(self, key):
        freq = self.key_freq[key]
        self.key_freq[key] = freq + 1
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.freq_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
        self._increment(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key_val:
            self.key_val[key] = value
            self._increment(key)
        else:
            if len(self.key_val) >= self.cap:
                # evict LRU from min_freq bucket
                evict, _ = self.freq_keys[self.min_freq].popitem(last=False)
                del self.key_val[evict]
                del self.key_freq[evict]
            self.key_val[key] = value
            self.key_freq[key] = 1
            self.freq_keys[1][key] = None
            self.min_freq = 1