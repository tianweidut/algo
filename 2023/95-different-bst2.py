class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n <= 0:
            return []

        def gen(choices):
            if not choices:
                return [None]

            all_trees = []
            for idx in range(0, len(choices)):
                val = choices[idx]
                left_trees = gen(choices=choices[:idx])
                right_trees = gen(choices=choices[idx + 1 :])
                for left in left_trees:
                    for right in right_trees:
                        all_trees.append(TreeNode(val=val, left=left, right=right))

            return all_trees

        return gen(choices=list(range(1, n+1)))
