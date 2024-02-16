# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        from collections import defaultdict

        levels = defaultdict(list)

        root.level = 0
        queue = [root]

        while queue:
            node = queue.pop(0)
            levels[node.level].append(node.val)

            if node.left:
                node.left.level = node.level + 1
                queue.append(node.left)

            if node.right:
                node.right.level = node.level + 1
                queue.append(node.right)

        return [sum(levels[idx]) / len(levels[idx]) for idx in range(0, len(levels))]
