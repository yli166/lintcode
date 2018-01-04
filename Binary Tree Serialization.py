"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import collections
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        string = ""
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            if not cur:
                string += ",#"
                continue
            else:
                string += "," + str(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
        return string

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        data = collections.deque(data.split(","))
        _, val = data.popleft(), data.popleft()
        root = None if val == "#" else TreeNode(int(val))
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                a, b = data.popleft(), data.popleft()
                cur.left = TreeNode(int(a)) if a != "#" else None
                cur.right = TreeNode(int(b)) if b != "#" else None
                queue.append(cur.left)
                queue.append(cur.right)
        return root
    # recursion
    # def deserialize(self, data):
    #     def doit():
    #         val = next(vals)
    #         if val == '#':
    #             return None
    #         node = TreeNode(int(val))
    #         node.left = doit()
    #         node.right = doit()
    #         return node
    #     vals = iter(data.split())
    #     return doit()