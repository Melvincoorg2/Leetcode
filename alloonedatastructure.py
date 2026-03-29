class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = self.next = None

class AllOne:

    def __init__(self):
        self.head = Node(0)        # dummy min sentinel
        self.tail = Node(float('inf'))  # dummy max sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node = {}         # key -> node

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_node:
            cur = self.head
            count = 1
        else:
            cur = self.key_node[key]
            count = cur.count + 1
            cur.keys.discard(key)

        # get or create node with count
        if cur.next.count == count:
            nxt = cur.next
        else:
            nxt = Node(count)
            self._insert_after(cur, nxt)

        nxt.keys.add(key)
        self.key_node[key] = nxt

        # clean up empty node
        if key in (self.key_node.get(key) and cur.keys or set()):
            pass
        if cur != self.head and not cur.keys:
            self._remove(cur)

    def dec(self, key: str) -> None:
        cur = self.key_node[key]
        count = cur.count - 1
        cur.keys.discard(key)

        if count == 0:
            del self.key_node[key]
        else:
            if cur.prev.count == count:
                prv = cur.prev
            else:
                prv = Node(count)
                self._insert_after(cur.prev, prv)
            prv.keys.add(key)
            self.key_node[key] = prv

        if not cur.keys:
            self._remove(cur)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))