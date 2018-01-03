"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        tmp, stack, total = root, [], 0
        while True:
            while root:
                stack.append(root)
                root = root.right
            if stack == []:
                return tmp
            node = stack.pop()
            total += node.val
            node.val = total
            root = node.left