# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        stack = [root]

        prev = TreeNode()
        while len(stack) != 0:
            node = stack.pop(-1)

            if node.left is None and node.right is None:
                prev.right = node
                prev.left = None
                prev = prev.right
            else:
                if node.right:
                    stack.append(node.right)
                    node.right = None

                if node.left:
                    stack.append(node.left)
                    node.left = None

                stack.append(node)

        return root
