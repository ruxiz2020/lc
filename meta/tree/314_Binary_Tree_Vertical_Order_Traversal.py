# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binary_tree(lst):
    if not lst or lst[0] is None:
        return None

    # Create the root of the tree
    root = TreeNode(lst[0])
    queue = [root]  # Queue to keep track of nodes to attach children to
    index = 1  # Start from the second element in the list

    while index < len(lst):
        node = queue.pop(0)

        # Add left child
        if index < len(lst) and lst[index] is not None:
            node.left = TreeNode(lst[index])
            queue.append(node.left)

        index += 1  # Move to the next element

        # Add right child
        if index < len(lst) and lst[index] is not None:
            node.right = TreeNode(lst[index])
            queue.append(node.right)

        index += 1  # Move to the next element

    return root

from collections import defaultdict
from typing import Optional, List
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, depth, offset):
            if root is None:
                return
            d[offset].append((depth, root.val))
            dfs(root.left, depth + 1, offset - 1)
            dfs(root.right, depth + 1, offset + 1)

        d = defaultdict(list)
        dfs(root, 0, 0)
        ans = []
        for _, v in sorted(d.items()):
            v.sort(key=lambda x: x[0])
            ans.append([x[1] for x in v])
        return ans


# Convert the list to binary tree
root_list = [3, 9, 20, None, None, 15, 7]
binary_tree_root = list_to_binary_tree(root_list)


res = Solution().verticalOrder(binary_tree_root)
print(res)
