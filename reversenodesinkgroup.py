# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
 def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

    dummy = ListNode(0, head)
    prev = dummy

    while True:
        # check if k nodes remain
        check = prev
        for _ in range(k):
            check = check.next
            if not check:
                return dummy.next

        # reverse k nodes
        cur = prev.next
        for _ in range(k - 1):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        prev = cur  # cur is now the tail of reversed group

    return dummy.next