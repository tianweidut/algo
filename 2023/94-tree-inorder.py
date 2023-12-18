# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.results = []
        self._do_inorder_r(root)
        return self.results

    def _do_inorder_r(self, root):
        """Recusive"""
        if root is None:
            return

        self._do_inorder_r(root.left)
        self.results.append(root.val)
        self._do_inorder_r(root.right)

    def _do_inorder_i(self, root):
        """Iteration"""
        ...
