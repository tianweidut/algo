class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        import sys
        self.max = -sys.maxsize 

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            self.max = max(self.max, node.val + left, node.val + right, left + right + node.val, node.val)
            return node.val + max(left, right, 0)

        dfs(root)
        return self.max
