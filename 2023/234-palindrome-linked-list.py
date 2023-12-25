# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return False

        stack = []
        trave_head = head
        while trave_head:
            stack.append(trave_head.val)
            trave_head = trave_head.next

        while head:
            if head.val != stack.pop(-1):
                return False
            head = head.next

        return True
