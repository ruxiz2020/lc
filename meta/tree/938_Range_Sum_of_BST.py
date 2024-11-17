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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            x = root.val
            ans = x if low <= x <= high else 0
            if x > low:
                ans += dfs(root.left)
            if x < high:
                ans += dfs(root.right)
            return ans

        return dfs(root)


lst = [10,5,15,3,7,18]; low = 7; high = 15
lst = [10,5,15,3,7,13,18,1,6]; low = 6; high = 10

root = list_to_bst(lst)
res = Solution().rangeSumBST(root, low, high)
print(res) # 32 # 23
