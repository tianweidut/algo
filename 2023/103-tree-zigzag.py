# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import defaultdict
        results = defaultdict(list)

        root.lvl = 0
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            results[node.lvl].append(node.val)
            if node.left:
                node.left.lvl = node.lvl + 1
                queue.append(node.left)
            if node.right:
                node.right.lvl = node.lvl + 1
                queue.append(node.right)

        rlist = []
        for i in range(0, len(results)):
            if i % 2 == 0:
                rlist.append(results[i])
            else:
                rlist.append(results[i][::-1])

        return rlist
