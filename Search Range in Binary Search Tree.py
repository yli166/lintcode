"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        stack = []
        res = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if stack == []:
                break
            node = stack.pop()
            if k1 <= node.val <= k2:
                res.append(node.val)
            root = node.right

        return res