# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        results = []
        root.lvl = 1
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)

            if node.lvl > len(results):
                results.append([])

            results[node.lvl - 1].append(node.val)

            if node.left:
                node.left.lvl = node.lvl + 1
                queue.append(node.left)
            
            if node.right:
                node.right.lvl = node.lvl + 1
                queue.append(node.right)

        return results
