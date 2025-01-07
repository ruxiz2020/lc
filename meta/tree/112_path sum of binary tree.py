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




def create_tree():
    """
    Creates the following binary tree:
            5
           / \
          4   8
         /   / \
        11  13  4
       /  \      \
      7    2      1
    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    return root

# Test the Solution
if __name__ == "__main__":
    tree = create_tree()
    solution = Solution()

    # Test case 1: target sum 22 (5->4->11->2)
    print(solution.hasPathSum(tree, 22))  # Expected output: True

    # Test case 2: target sum 26 (5->8->13)
    print(solution.hasPathSum(tree, 26))  # Expected output: True

    # Test case 3: target sum 27 (5->8->4->1 + ???) - path does not exist
    print(solution.hasPathSum(tree, 27))  # Expected output: False

    # Test case 4: target sum 0 on a non-empty tree - path does not exist
    print(solution.hasPathSum(tree, 0))   # Expected output: False