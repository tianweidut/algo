# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        sentry = ListNode(next=head)
        head = sentry

        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return sentry.next
