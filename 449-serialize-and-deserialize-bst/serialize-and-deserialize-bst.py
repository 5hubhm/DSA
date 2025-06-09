# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Serialize BST using preorder traversal
    def serialize(self, root):
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        vals = []
        preorder(root)
        return ",".join(vals)

    # Deserialize BST using preorder + bounds
    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split(",")))
        index = [0]  # use a list so it’s mutable in nested function

        def build(min_val, max_val):
            if index[0] == len(vals):
                return None
            val = vals[index[0]]
            if val < min_val or val > max_val:
                return None
            index[0] += 1
            node = TreeNode(val)
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            return node

        return build(float('-inf'), float('inf'))
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans