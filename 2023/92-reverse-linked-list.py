# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head

        sentry = ListNode(next=head)
        prev = sentry

        idx = 1
        while head:
            if idx < left:
                idx += 1
                prev = head
                head = head.next
            else:
                _prev = None
                while idx < right:
                    _next = head.next
                    head.next = _prev
                    _prev = head
                    head = _next
                    idx += 1
                    
                last = head.next
                prev.next.next = last
                prev.next = head
                head.next = _prev
                break

        return sentry.next
