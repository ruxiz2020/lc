class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        self.getAllDepth(root)

        left_depth = root.left.val if root.left else 0
        right_depth = root.right.val if root.right else 0
        if abs(left_depth - right_depth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def getAllDepth(self, root):
        if root == None:
            return 0
        root.val = 1 + max(self.getAllDepth(root.left),
                           self.getAllDepth(root.right))
        return root.val
