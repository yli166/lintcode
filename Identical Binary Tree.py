"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

import collections


class Solution:
    """
    @param: a: the root of binary tree a.
    @param: b: the root of binary tree b.
    @return: true if they are identical, or false.
        """

    # def isSameTree1(self, a, b):
    #     if a and a:
    #         return b.val == a.val and self.isSameTree(b.left, a.left) and self.isSameTree(b.right, a.right)
    #     else:
    #         return a == b


    # BFS
    def isIdentical(self, a, b):
        stack = collections.deque([(a, b)])
        while stack:
            node1, node2 = stack.popleft()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        return True