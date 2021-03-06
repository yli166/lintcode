"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(path + str(root.val))
        if root.left:
            self.dfs(root.left, path + str(root.val) + '->', res)
        if root.right:
            self.dfs(root.right, path + str(root.val) + '->', res)