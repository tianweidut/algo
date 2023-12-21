# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def _travel(node, prev_sum):
            if node is None: return False

            if node.left is None and node.right is None:
                return prev_sum + node.val == targetSum

            prev_sum += node.val
            return _travel(node.left, prev_sum) or _travel(node.right, prev_sum)

        return _travel(root, 0)
