import collections


class Solution:
    """
    @param: : the given tree
    @return: Whether it is a full tree
    """

    def isFullTree(self, root):
        if not root:
            return True
        stack = collections.deque([(root)])
        while stack:
            node = stack.popleft()
            if not node.left and not node.right:
                continue
            elif node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)
            else:
                return False

        return True