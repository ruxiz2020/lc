# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root, value):
    if not root:
        return TreeNode(value)
    if value < root.val:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def list_to_bst(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])  # The first element is the root
    for value in lst[1:]:
        insert_into_bst(root, value)  # Insert each remaining element into the BST
    return root

class Solution:
    """
    This solution searches a binary search tree (BST) to find the value
    closest to the given target. At each node, it compares the current node's
    value to the best known answer so far (res) and updates if it finds a closer match.

    Time Complexity: O(H) on average,
      where H is the height of the BST (often O(log N) if the tree is balanced).
      In the worst case of a skewed tree, it can be O(N).

    Space Complexity: O(1),
      we only store a few variables (res and temporary pointers).
    """
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Initialize 'res' to the root's value as a starting reference.
        res = root.val

        # Traverse the BST from the root downward.
        while root:
            # Update 'res' if the current node's value is closer to 'target'
            # than the previously recorded 'res'.
            #
            # We use a custom 'key' in min() to compare two values (res, root.val)
            # by how close they are to 'target'.
            #   - abs(target - x) measures the distance from 'target'.
            #   - x is used as a tiebreaker if distances are equal
            #     (for deterministic behavior, though not strictly required here).
            res = min(res, root.val, key=lambda x: (abs(target - x), x))

            # If 'target' is less than the current node's value,
            # we move to the left subtree (where values are smaller).
            # Otherwise, move to the right subtree (where values are larger).
            if target < root.val:
                root = root.left
            else:
                root = root.right

        # After traversing down the BST, return the value 'res'
        # which should be the closest to 'target'.
        return res



root_list = [4,2,5,1,3]; target = 3.714286

bst_root = list_to_bst(root_list)

res = Solution().closestValue(bst_root, target)
print(res) # 4
