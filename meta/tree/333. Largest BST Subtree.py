import math
from dataclasses import dataclass


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math

# A small helper class to store information about a subtree:
# - mn (int):  the minimum value in the subtree
# - mx (int):  the maximum value in the subtree
# - size (int): the number of nodes in this subtree if it's a valid BST;
#               otherwise the size of the largest BST subtree found so far in its children.
class T:
    def __init__(self, mn, mx, size):
        self.mn = mn   # Minimum value in this subtree
        self.mx = mx   # Maximum value in this subtree
        self.size = size  # Size of the subtree if BST, or largest BST size among children if invalid

class Solution:
    """
    Finds the size of the largest subtree that is a valid BST.

    Time Complexity: O(N), where N is the number of nodes in the tree,
      since we perform a post-order DFS visit of each node exactly once.
    Space Complexity: O(H), where H is the height of the tree,
      reflecting the maximum depth of the recursion stack.
      (In the worst case of a skewed tree, H can be O(N).)
    """

    def largestBSTSubtree(self, root: 'TreeNode') -> int:
        """
        Returns the size of the largest BST subtree in the given binary tree.
        """
        def dfs(node: 'TreeNode') -> T:
            """
            Perform a post-order DFS. For each node, return a T object that includes:
              - mn, mx: the min and max values within this subtree
              - size: the size of the subtree if it's a valid BST; otherwise,
                      the largest BST subtree size found in the children.
            """
            # Base case: If the node is None, it's a valid BST by definition (size=0).
            if not node:
                return T(math.inf, -math.inf, 0)

            # Recursively process the left subtree
            left_info = dfs(node.left)
            # Recursively process the right subtree
            right_info = dfs(node.right)

            # Check BST property for the current node:
            # - The current node's value must be > max value in the left subtree (left_info.mx)
            # - The current node's value must be < min value in the right subtree (right_info.mn)
            if left_info.mx < node.val < right_info.mn:
                # If valid BST, compute updated min, max, and size for this subtree
                mn = min(left_info.mn, node.val)
                mx = max(right_info.mx, node.val)
                size = 1 + left_info.size + right_info.size
                return T(mn, mx, size)
            else:
                # If not a valid BST:
                # - We use -inf and inf to invalidate this subtree for any parent checks.
                # - We carry forward the maximum size encountered in its children.
                return T(-math.inf, math.inf, max(left_info.size, right_info.size))

        # Begin DFS from the root, and return the 'size' field indicating the largest BST subtree.
        return dfs(root).size

