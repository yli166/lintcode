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
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root == None:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        if not root:
            return 0
        stack = collections.deque([(root, 1)])
        count = 0
        while stack:
            node, level = stack.popleft()
            if node:
                count = max(count,level)
                stack.append((node.left,level + 1))
                stack.append((node.right,level + 1))
        return count