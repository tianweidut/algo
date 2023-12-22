# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        fast = slow = head
        is_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                is_cycle = True
                break

        if not is_cycle:
            return None

        slow = head
        while True:
            if slow is fast:
                return slow
            slow = slow.next
            fast = fast.next
