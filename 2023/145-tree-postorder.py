# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.results = []
        self._do_postorder_i(root)
        return self.results

    def _do_postorder_i(self, root):
        if not root:
            return

        stack = [root]
        while len(stack) != 0:
            node = stack[-1]

            if node.left is not None:
                stack.append(node.left)
                node.left = None
            elif node.right is not None:
                stack.append(node.right)
                node.right = None
            else:
                self.results.append(node.val)
                stack.pop(-1)

    def _do_postorder_r(self, root):
        if not root:
            return

        self._do_postorder_r(root.left)
        self._do_postorder_r(root.right)
        self.results.append(root.val)
