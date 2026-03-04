def insertionSortList(self, head):

        dummy = ListNode(0)  # start of sorted list
        current = head

        while current:

            prev = dummy

            # find position to insert
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            next_node = current.next

            # insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next