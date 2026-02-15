def deleteDuplicates(self, head):

        current = head

        while current and current.next:

            if current.val == current.next.val:
                # Skip duplicate node
                current.next = current.next.next
            else:
                current = current.next

        return head