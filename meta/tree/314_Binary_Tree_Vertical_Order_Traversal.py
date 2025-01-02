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
    """
    This code performs a vertical order traversal of a binary tree by using 
    a DFS approach to group node values by their column offsets, 
    where the offset is adjusted relative to the root 
    (left child decreases offset, right child increases it).

    During the traversal, node values and their depths are stored 
    in a dictionary keyed by offset, and the dictionary is later 
    processed by sorting the offsets (columns) and sorting 
    node values within each column by depth to ensure 
    upper nodes appear before lower nodes.

    Time Complexity: O(N log N)
      - DFS visits each node once, O(N).
      - Sorting by offset can be O(K log K), where K is the number of unique offsets (<= N).
      - Sorting each column by depth also costs time, but typically still bounded by O(N log N) overall.

    Space Complexity: O(H + N)
      - O(N) for storing all node information in the dictionary.
      - O(H) recursion stack in the worst case (H is the height of the tree).
      - In a balanced tree H = O(log N), in worst case (skewed tree) H = O(N).
    """

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # A helper DFS function that populates the dictionary 'd' with
        # key = offset (column index),
        # value = list of (depth, node_value) tuples.
        def dfs(node, depth, offset):
            if node is None:
                return
            # Append the tuple (depth, node's value) to the list corresponding to 'offset'.
            d[offset].append((depth, node.val))

            # Go to left child: depth + 1, offset - 1
            dfs(node.left, depth + 1, offset - 1)
            # Go to right child: depth + 1, offset + 1
            dfs(node.right, depth + 1, offset + 1)

        from collections import defaultdict
        d = defaultdict(list)  # Dictionary to hold column_offset -> list of (depth, value)

        # Populate the dictionary using DFS, starting at offset = 0, depth = 0
        dfs(root, 0, 0)

        # Prepare the final answer
        ans = []

        print(d)  # Debug print, e.g. {0: [(0, 3), (2, 15)], -1: [(1, 9)], 1: [(1, 20)], 2: [(2, 7)]}

        # 1. Sort dictionary items by their key (offset).
        # 2. Each value (list of (depth, val)) is then sorted by 'depth'.
        # 3. Extract the node values (ignoring depth now that it's sorted).
        for _, nodes in sorted(d.items()):  # Sort by offset
            # Sort each list by depth so that upper nodes come before lower nodes.
            nodes.sort(key=lambda x: x[0])  # Sort by x[0] which is the 'depth'
            # Append just the node values (x[1]) to ans.
            ans.append([x[1] for x in nodes])

        return ans



# Convert the list to binary tree
root_list = [3, 9, 20, None, None, 15, 7]
binary_tree_root = list_to_binary_tree(root_list)


res = Solution().verticalOrder(binary_tree_root)
print(res) # [[9], [3, 15], [20], [7]]
