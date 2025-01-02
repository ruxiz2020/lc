# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This code checks whether a binary tree has a root-to-leaf path 
    where the sum of the node values equals a given target summ,
      using a recursive approach to traverse the tree.

    At each node, it subtracts the current node's value from the 
    target sum and recursively checks both the left and right subtrees, 
    returning True if a valid path is found or False if the 
    traversal reaches a null node or no valid path exists.

    The time complexity is 
    O(N), where 
    N is the number of nodes in the tree, as each node is visited once, 
    and the space complexity is 
    O(H), where 
    H is the height of the tree, due to the recursion stack.
    O(N)
    O(H)
    """
    def hasPathSum(self, root: TreeNode, summ: int) -> bool:
        if not root:
            return False
        if root.val == summ and not root.left and not root.right:
            return True
        return (self.hasPathSum(root.left, summ - root.val) or
                self.hasPathSum(root.right, summ - root.val))


root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetSum = 22
