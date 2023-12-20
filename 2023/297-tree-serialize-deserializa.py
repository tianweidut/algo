# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        results = []
        def _pre(node):
            if not node:
                results.append("#")
                return

            results.append(str(node.val))
            _pre(node.left)
            _pre(node.right)

        _pre(root)
        return ",".join(results)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(",")
        def _pre():
            val = nodes.pop(0)
            if val == "#":
                return None
            else:
                node = TreeNode(val=int(val))
                node.left = _pre()
                node.right = _pre()
                return node

        return _pre()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
