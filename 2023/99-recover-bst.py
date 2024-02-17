# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        m1, m2 = None, None
        prev = None

        def _inorder(node):
            nonlocal m1, m2, prev
            if not node:
                return

            _inorder(node.left)
            if prev is not None and prev.val > node.val:
                if m1 is None:
                    m1 = prev
                m2 = node

            prev = node
            _inorder(node.right)

        _inorder(root)
        m1.val, m2.val = m2.val, m1.val
