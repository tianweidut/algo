# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0

        def _travel(node):
            if not node:
                return
            
            _travel(node.right)

            node.val = node.val + self.sum
            self.sum = node.val

            _travel(node.left) 

        _travel(root)
        return root

