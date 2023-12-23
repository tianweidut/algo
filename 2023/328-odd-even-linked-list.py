# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first, second = head, head.next
        sentry_second = second

        while first and first.next and second and second.next:
            first.next = second.next
            first = first.next
            second.next = first.next
            second = second.next

        first.next = sentry_second
        return head

