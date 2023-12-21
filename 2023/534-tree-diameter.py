# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = 0
        def _depth(node):
            left = (_depth(node.left) + 1) if node.left else 0
            right = (_depth(node.right) + 1) if node.right else 0

            self.ans = max(self.ans, left + right)
            return max(left, right)

        _depth(root)
        return self.ans
