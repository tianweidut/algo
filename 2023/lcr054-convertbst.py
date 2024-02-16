class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        sums = 0
        def _travel(node):
            nonlocal sums
            if not node:
                return
            
            _travel(node.right)
            sums += node.val
            node.val = sums
            _travel(node.left)

        _travel(root)
        return root
