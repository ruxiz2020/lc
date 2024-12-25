import math
from dataclasses import dataclass


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

@dataclass(frozen=True)
class T:
    mn: int  # the minimum value in the subtree
    mx: int  # the maximum value in the subtree
    size: int  # the size of the subtree


class Solution:
    """
    O(N)
    O(H)
    """
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> T:
            # Base case: If the node is None (empty subtree), it is a valid BST.
            # Return:
            # - `mn` as `inf` since no valid nodes exist to limit the range.
            # - `mx` as `-inf` for the same reason.
            # - `size` as `0` since there are no nodes in this subtree.
            if not root:
                return T(math.inf, -math.inf, 0)

            # Recursive call for the left subtree.
            l = dfs(root.left)

            # Recursive call for the right subtree.
            r = dfs(root.right)

            # Check if the current node can form a valid BST with its left and right subtrees.
            # Condition:
            # - The maximum value in the left subtree (`l.mx`) should be less than the current node value.
            # - The current node value should be less than the minimum value in the right subtree (`r.mn`).
            if l.mx < root.val < r.mn:
                # If valid, update:
                # - `mn`: The minimum value of the subtree (either the left subtree or the current node).
                # - `mx`: The maximum value of the subtree (either the right subtree or the current node).
                # - `size`: Add 1 (for the current node) to the size of the left and right BST subtrees.
                return T(min(l.mn, root.val), max(r.mx, root.val), 1 + l.size + r.size)

            # If the current subtree is not a valid BST:
            # - Return `(-inf, inf)` to invalidate this subtree for further parent node checks.
            # - Pass the largest size between the left and right subtrees up the recursion chain.
            return T(-math.inf, math.inf, max(l.size, r.size))

        # Start the DFS from the root and return the size of the largest BST subtree.
        return dfs(root).size
