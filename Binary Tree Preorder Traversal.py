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
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        if not root:
            return []
        stack = collections.deque([(root)])
        res = []
        while stack:
            node = stack.popleft()
            res.append(node.val)
            if node.right:
                stack.appendleft(node.right)
            if node.left:
                stack.appendleft(node.left)

        return res