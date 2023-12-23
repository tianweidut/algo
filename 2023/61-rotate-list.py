# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 0
        node = head
        while node:
            node = node.next
            n += 1

        step = n - k % n
        if step == n:
            return head

        sentry_head = node = ListNode(next=head)
        n = 0
        while n < step:
            node = node.next
            n += 1

        new_head = travel_node = node.next
        node.next = None

        while travel_node and travel_node.next:
            travel_node = travel_node.next

        travel_node.next = sentry_head.next
        return new_head
