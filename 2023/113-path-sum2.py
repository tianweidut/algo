# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.results = []

        def _travel(node, record_paths, prev_sum):
            if node is None:
                return

            if node.left is None and node.right is None:
                if node.val + prev_sum == targetSum:
                    self.results.append(record_paths + [node.val])
                return

            prev_sum += node.val
            record_paths.append(node.val)
            _travel(node.left, record_paths.copy(), prev_sum)
            _travel(node.right, record_paths.copy(), prev_sum)

        _travel(root, [], 0)
        return self.results
