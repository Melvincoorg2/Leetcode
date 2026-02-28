def copyRandomList(self, head):

        if not head:
            return None

        # Step 1: create mapping
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: connect next and random
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]