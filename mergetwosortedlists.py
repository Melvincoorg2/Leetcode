def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)
        tail = dummy

        p1 = list1
        p2 = list2

        while p1 and p2:

            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next

            tail = tail.next

        # Attach remaining nodes
        if p1:
            tail.next = p1
        else:
            tail.next = p2

        return dummy.next