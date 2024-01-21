# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = []
        to_delete_map = {k:True for k in to_delete}

        def _dfs(node):
            if not node:
                return None

            node.left = _dfs(node.left)
            node.right = _dfs(node.right)
            if node.val in to_delete_map:
                if node.left:
                    roots.append(node.left)

                if node.right:
                    roots.append(node.right)
                return None
            else:
                return node

        node = _dfs(root)
        if node:
            roots.append(node)

        return roots
