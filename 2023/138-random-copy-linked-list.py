"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        sentry_copy_head = copy_head = Node(x=0)

        sentry_head = head
        idx = 0
        copy_node_map = {}
        while head:
            copy_head.next = Node(x=head.val)
            copy_head.next.idx = idx
            copy_head = copy_head.next
            copy_node_map[idx] = copy_head

            head.idx = idx
            head = head.next
            idx += 1

        head = sentry_head
        copy_head = sentry_copy_head.next
        while head:
            if head.random:
                random_idx = head.random.idx
                copy_head.random = copy_node_map[random_idx]
            head = head.next
            copy_head = copy_head.next

        return sentry_copy_head.next
