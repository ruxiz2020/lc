from collections import defaultdict, deque
from typing import Optional, List

# Minimal TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []

        # This dictionary will map each column index to a list of (row, node_value) tuples.
        # Keys: column indices (which can be negative, zero, or positive)
        # Values: list of tuples (row, node.val)
        node_data = defaultdict(list)

        # We'll use a queue for BFS (level-order traversal).
        # Each element in the queue is a tuple of (node, row, column).
        # - node: the current TreeNode
        # - row: the vertical level (distance from the root vertically)
        # - column: the horizontal index (distance from the root horizontally)
        queue = deque([(root, 0, 0)])  # Start with the root at row=0, col=0

        # Perform BFS to populate node_data
        while queue:
            # Pop the front of the queue
            node, row, col = queue.popleft()

            # Append the (row, node value) tuple to the corresponding column list
            node_data[col].append((row, node.val))

            # If the current node has a left child, add it to the queue.
            # Note that the left child's column is col - 1, and its row is row + 1.
            if node.left:
                queue.append((node.left, row + 1, col - 1))

            # If the current node has a right child, add it to the queue.
            # The right child's column is col + 1, and its row is row + 1.
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        # Prepare the final result list
        result = []
        # defaultdict(<class 'list'>, {0: [(0, 3), (2, 15)], -1: [(1, 9)], 1: [(1, 20)], 2: [(2, 7)]})
        print(node_data)

        # Sort by column index, because we want the leftmost columns first.
        for col in sorted(node_data.keys()):
            # For each column, we have a list of (row, value) pairs.
            # Sort by 'row' first so that nodes on upper rows come before lower rows.
            # If row is the same, Python's sort is stable and will keep the original order,
            # but typically we also want ascending order of node.val if rows tie
            # (the problem specification may vary). If needed, we could do
            # sorted(node_data[col], key=lambda x: (x[0], x[1]))
            column_nodes = sorted(node_data[col])

            # We only need the values in the final output, so we extract just the node values.
            result.append([val for row, val in column_nodes])

        return result




# -----------------------------
# HELPER CODE FOR TESTING
# -----------------------------
def build_tree_from_list(lst, index=0):
    """
    Build a binary tree from a list (like a level-order serialization).
    None values represent missing children.

    :param lst: List of values or None, representing the level-order traversal of a binary tree.
    :param index: Current index in the list.
    :return: Root of the binary tree.
    """
    if index >= len(lst) or lst[index] is None:
        return None

    root = TreeNode(lst[index])
    # For a level-order list, left child index is 2 * index + 1, right child is 2 * index + 2
    root.left = build_tree_from_list(lst, 2 * index + 1)
    root.right = build_tree_from_list(lst, 2 * index + 2)
    return root

def print_test_result(description, root_list):
    """
    Build a tree from `root_list`, call verticalTraversal on it,
    and print the result.
    """
    root = build_tree_from_list(root_list)
    solution = Solution()
    result = solution.verticalTraversal(root)
    print(description)
    print("Tree (level-order):", root_list)
    print("Vertical Traversal:", result)
    print("-" * 50)

# -----------------------------
# TEST CASES
# -----------------------------
if __name__ == "__main__":
    # 1) Example with a small balanced tree
    print_test_result("Test Case 1", [3, 9, 20, None, None, 15, 7])
    # Expected vertical traversal might look like [[9],[3,15],[20],[7]]

    # 2) A slightly more complex tree
    # Level-order: [1,2,3,4,6,5,7,None,None,None,None,None,None,None,8]
    # This tree structure is:
    #           1
    #         /   \
    #        2     3
    #       / \   / \
    #      4   6 5   7
    #                 \
    #                  8
    # (Some internal Nones for missing children in the array representation.)
    print_test_result("Test Case 2", [1,2,3,4,6,5,7,None,None,None,None,None,None,None,8])
    # Expected output structure could be something like:
    # [[4],[2],[1,6,5],[3],[7],[8]]

    # 3) Single node tree
    print_test_result("Test Case 3", [42])
    # Expected vertical traversal: [[42]]

    # 4) Empty tree
    # If you pass an empty list, the tree is None
    print_test_result("Test Case 4 (empty tree)", [])
    # Expected vertical traversal: []
