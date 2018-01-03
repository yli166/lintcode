"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return:
    """

    # DFS
    # def flatten(self, root):
    #     if not root:
    #         return

    # node = root

    # while node:
    #     if node.left:
    #         pre = node.left
    #         while pre.right:
    #             pre=pre.right
    #         pre.right=node.right
    #         node.right=node.left
    #         node.left=None
    #     node = node.right
    # return root

    # DFS
    def flatten(self, root):
        # write your code here
        if root == None:
            return root
        stack = [root]
        while stack != []:
            node = stack.pop()
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
            node.left = None
            if stack == []:
                node.right = None
            else:
                node.right = stack[len(stack) - 1]

                # #pre = pre.next 移动光标
                # pre = node.left 移动光标
                # #pre.val = None 改变数值
                # #pre.right = node.right 改变数值