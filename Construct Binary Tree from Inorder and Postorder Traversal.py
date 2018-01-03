class Solution:
    """
    @param: inorder: A list of integers that inorder traversal of a tree
    @param: postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """

    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        top = postorder[-1]
        root = TreeNode(top)
        for i in range(len(inorder)):
            if inorder[i] == top:
                break

        root.left = self.buildTree(inorder[: i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        return root