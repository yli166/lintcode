"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):

        if not inorder:
            return None
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break
        root.left = self.buildTree(preorder[1 : 1 + i], inorder[ : i])
        root.right = self.buildTree(preorder[i + 1 : ], inorder[i + 1 : ])
        return root