# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        val = preorder[0]
        idx = inorder.index(val)
        return TreeNode(
            val=val,
            left=self.buildTree(preorder[1:idx+1], inorder[0:idx]),
            right=self.buildTree(preorder[idx+1:], inorder[idx+1:]),
        )
