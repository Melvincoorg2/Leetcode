def findKthNumber(n, k):

    def count_nodes(prefix, n):
        # count numbers in [1,n] that start with this prefix
        total = 0
        curr, next_ = prefix, prefix + 1
        while curr <= n:
            total += min(n + 1, next_) - curr
            curr *= 10
            next_ *= 10
        return total

    curr = 1
    k -= 1  # already at node 1

    while k > 0:
        count = count_nodes(curr, n)
        if count <= k:
            # skip entire subtree, go to next sibling
            k -= count
            curr += 1
        else:
            # go deeper into subtree
            k -= 1
            curr *= 10

    return curr