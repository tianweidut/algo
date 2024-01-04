    def rob(self, root) -> int:
        def _dfs(node):
            if not node:
                return 0, 0

            left_rob, left_non_rob = _dfs(node.left)
            right_rob, right_non_rob = _dfs(node.right)

            return (
                node.val + left_non_rob + right_non_rob,
                max(left_rob, left_non_rob) + max(right_rob, right_non_rob),
            )

        return max(_dfs(root))
