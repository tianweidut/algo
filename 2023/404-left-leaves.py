# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sums = 0
        def _travel(node):
            if not node:
                return

            nonlocal sums

            if node.left:
                left = node.left
                if not left.left and not left.right:
                    sums += left.val
                _travel(node.left)

            _travel(node.right)    

        _travel(root)
        return sums
