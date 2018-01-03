"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []
        cur = root.val
        res = [[cur]]
        stack = [root]
        queue = []
        count = 1
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            count -= 1
            if count == 0:
                queue=[x.val for x in stack]
                res+=[queue] if queue else []
                count = len(stack)
        return res