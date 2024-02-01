# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return

        res = []
        def dfs(node, parents):
            if node.left is None and node.right is None:
                res.append("->".join([str(p) for p in parents]))
                return

            if node.left:
                parents.append(node.left.val)
                dfs(node.left, parents.copy())
                parents.pop(-1)

            if node.right:
                parents.append(node.right.val)
                dfs(node.right, parents.copy())
                parents.pop(-1)

        dfs(node=root, parents=[root.val])
        return res
