# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        left, right = self.split(head)
        left, right = self.sortList(left), self.sortList(right)
        return self.merge(left, right)

    def split(self, head):
        left = head
        fast = slow = ListNode(next=head)

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right = slow.next
        slow.next = None
        return left, right

    def merge(self, head1, head2):
        sentry_node = ListNode()
        head = sentry_node

        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        
        if head1:
            head.next = head1

        if head2:
            head.next = head2

        return sentry_node.next
