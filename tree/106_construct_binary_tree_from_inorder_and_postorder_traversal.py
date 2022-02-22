# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        index = inorder.index(postorder.pop())
        root = TreeNode(inorder[index])

        root.right = self.buildTree(inorder[index + 1:len(inorder)], postorder)
        root.left = self.buildTree(inorder[0:index], postorder)

        return root  
