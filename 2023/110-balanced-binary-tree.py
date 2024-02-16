# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _chk(node):
            if not node:
                return True, 0

            left_b, left_l = _chk(node.left)
            right_b, right_l = _chk(node.right)

            return left_b and right_b and abs(left_l - right_l) <= 1, max(left_l, right_l) + 1

        _is_balance, _ = _chk(root)
        return _is_balance
        

        
