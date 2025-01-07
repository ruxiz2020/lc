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




def create_tree():
    """
    Create the following binary tree:
            3
           / \
          9  20
            /  \
           15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

if __name__ == "__main__":
    tree = create_tree()
    solution = Solution()
    result = solution.verticalTraversal(tree)
    print("Vertical traversal of the tree:", result)
    # Expected output: [[9],[3,15],[20],[7]]
