# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        current = head

        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next

            current = current.next

        # important: end after list
        after.next = None

        # connect both lists
        before.next = after_head.next

        return before_head.next