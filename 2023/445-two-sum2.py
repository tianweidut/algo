# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r_l1 = self.reverse(l1)
        r_l2 = self.reverse(l2)

        node = head = ListNode()
        acc = 0
        while r_l1 or r_l2:
            val = acc
            if r_l1:
                val += r_l1.val
                r_l1 = r_l1.next

            if r_l2:
                val += r_l2.val
                r_l2 = r_l2.next

            acc = val // 10
            node.next = ListNode(val=val % 10)
            node = node.next

        if acc != 0:
            node.next = ListNode(val=acc)

        return self.reverse(head.next)


    def reverse(self, head):
        if not head or not head.next:
            return head

        root = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return root
