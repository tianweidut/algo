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
        self._do_inorder_i(root)
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
        if root is None:
            return

        stack = [root]

        while len(stack) != 0:
            node = stack.pop(-1)

            if node.right is None and node.left is None:
                self.results.append(node.val)
                continue

            if node.right is not None:
                stack.append(node.right)
                node.right = None

            stack.append(node)

            if node.left is not None:
                stack.append(node.left)
                node.left = None
