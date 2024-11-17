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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val

        while root:
            res = min(res, root.val, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right
        return res


root_list = [4,2,5,1,3]; target = 3.714286

bst_root = list_to_bst(root_list)

res = Solution().closestValue(bst_root, target)
print(res)
