# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.target = None
        self._chkin(root, p, q)
        return self.target

    def _chkin(self, root, p, q) -> bool:
        # check p or q in root tree, return boolean
        if not root:
            return False

        in_left = self._chkin(root.left, p, q)
        in_right = self._chkin(root.right, p, q)

        if (in_left and in_right):
            self.target = root

        if (in_left or in_right) and ((root.val == p.val) or (root.val == q.val)):
            self.target = root

        return (in_left or in_right) or (root.val == p.val) or (root.val == q.val)
