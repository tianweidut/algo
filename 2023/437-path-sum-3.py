# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = 0

        def _travel(node, stack):
            if not node:
                return

            stack.append(node.val + stack[-1])
            for i in range(0, len(stack) -1):
                if stack[-1] - stack[i] == targetSum:
                    self.cnt += 1

            _travel(node.left, stack.copy())
            _travel(node.right, stack.copy())

        _travel(root, [0])
        return self.cnt

    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = 0

        def _travel(node, stack):
            if not node:
                return

            stack.append(node.val)
            for idx in range(0, len(stack)):
                if targetSum == sum(stack[idx:]):
                    self.cnt += 1

            _travel(node.left, stack.copy())
            _travel(node.right, stack.copy())

        _travel(root, [])
        return self.cnt
