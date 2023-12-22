# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        import sys

        self.max = -sys.maxsize

        def _travel(node) -> int:
            if not node:
                return -sys.maxsize
            
            left = _travel(node.left)
            right =_travel(node.right)

            # define _travel: from the current to child, record max and return path max
            self.max = max(self.max, left + node.val, right + node.val, node.val, node.val + left + right)
            return max(left + node.val, node.val, right+node.val)

        _travel(root)
        return self.max
