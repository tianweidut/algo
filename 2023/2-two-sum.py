# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = head = ListNode()
        acc = 0
        while l1 or l2:
            val = acc
            if l1:
                val += l1.val
                l1 = l1.next

            if l2:
                val += l2.val
                l2 = l2.next

            acc = val // 10
            node.next = ListNode(val=val % 10)
            node = node.next

        if acc != 0:
            node.next = ListNode(val=acc)

        return head.next
