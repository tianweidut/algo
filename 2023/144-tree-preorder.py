# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.results = []
        self._preorder_i(root)
        return self.results

    def _preorder_r(self, root):
        if root is None:
            return

        self.results.append(root.val)
        self._preorder_r(root.left)
        self._preorder_r(root.right)

    def _preorder_i(self, root):
        if not root:
            return

        stack = [root]

        while len(stack) != 0:
            node = stack.pop(-1)

            self.results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
