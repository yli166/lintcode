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
    @param: root: The root of binary tree
    @return: An integer
    """

    # recursion

    # def minDepth(self, root):
    #     if not root:
    #         return 0
    #     if not root.left:
    #         return self.minDepth(self, root.right) + 1
    #     if not root.right:
    #         return self.minDepth(self, root.left) + 1
    #     return 1 + min(self.minDepth(root.left),self.minDepth(root.right))

    # bfs
    def minDepth(self, root):
        if not root:
            return 0
        stack = collections.deque([(root, 1)])
        while stack:
            node, level = stack.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    stack.append((node.left, level + 1))
                    stack.append((node.right, level + 1))
