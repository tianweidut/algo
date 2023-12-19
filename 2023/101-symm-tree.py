# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self._check(root.left, root.right)

    def _check(self, p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False

        return p.val == q.val and self._check(p.left, q.right) and self._check(p.right, q.left) 

