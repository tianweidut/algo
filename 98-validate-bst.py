# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        
        return self._is_bst(root, -sys.maxsize, sys.maxsize)

    def _is_bst(self, root, min_val, max_val):
        if root is None:
            return True
        
        return  ((min_val < root.val < max_val) and 
                 self._is_bst(root.left, min_val, root.val) and 
                 self._is_bst(root.right, root.val, max_val)) 
