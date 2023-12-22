# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        len_a = 0
        node = head_a
        while node:
            node = node.next
            len_a += 1

        len_b = 0
        node = head_b
        while node:
            node = node.next
            len_b += 1

        if len_a <= len_b:
            diff = len_b - len_a
            while diff:
                head_b = head_b.next
                diff -= 1
        else:
            diff = len_a - len_b
            while diff:
                head_a = head_a.next
                diff -= 1

        while head_a and head_b:
            if head_a is head_b:
                return head_a
            head_a = head_a.next
            head_b = head_b.next

        return None
