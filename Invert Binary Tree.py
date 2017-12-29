"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invertBinaryTree(self, root):
        # if not root:
        #     return None
        # root.left,root.right = root.right,root.left
        # self.invertBinaryTree(root.left)
        # self.invertBinaryTree(root.right)
        # return root


        # BFS
        # queue = collections.deque([(root)])
        # while queue:
        #     node = queue.popleft()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         queue.append(node.left)
        #         queue.append(node.right)
        # return root


        # DFS
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
        return root