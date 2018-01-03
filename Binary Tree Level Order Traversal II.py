"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):
        if not root:
            return []
        stack = [root]
        count = 1
        res = [[root.val]]
        queue = []
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            count -= 1
            if count == 0:
                queue = [x.val for x in stack]
                res += [queue] if queue else []
                count = len(stack)
        res = res[::-1]
        return res
