# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = []
        if root is None:
            return True
        queue.append(root)
        flag = False
        while queue:
            node = queue.pop(0)
            if flag is False:
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    flag = True # not complete row found
                    if node.left:
                        queue.append(node.left)
                    elif node.right:
                        return False
            elif flag is True:
                if node.left or node.right:
                    return False
        return True
