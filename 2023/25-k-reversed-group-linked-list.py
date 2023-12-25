# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head

        def _reverse_first_k(head, k):
            _cnt = 0
            _travel = head
            while _cnt < k and _travel:
                _travel = _travel.next
                _cnt += 1

            if _cnt != k:
                return head, _travel, False

            _cnt = 0
            _prev = None
            while _cnt < k:
                _cnt += 1
                _next = head.next
                head.next = _prev
                _prev = head
                head = _next

            return _prev, head, True

        sentry_head = ListNode(next=head)
        prev = sentry_head
        while True:
            if not head or not head.next:
                break

            head, tail, is_reverse = _reverse_first_k(head, k)
            if not is_reverse:
                break
                
            _prev_next = prev.next
            prev.next.next = tail
            prev.next = head
            head = tail
            prev = _prev_next

        return sentry_head.next
