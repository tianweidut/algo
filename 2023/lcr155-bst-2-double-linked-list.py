"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        stack = []
        first = None
        prev = None
        cur = root
        last = None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop(-1)
            last = cur
            if prev is None:
                first = cur
            else:
                prev.right = cur
                cur.left = prev

            prev = cur
            cur = cur.right

        first.left = last
        last.right = first
            
        return first
        
