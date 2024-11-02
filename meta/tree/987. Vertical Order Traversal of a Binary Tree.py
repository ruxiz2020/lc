from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        node_data = defaultdict(list)  # {column: [(row, value)]}

        queue = deque([(root, 0, 0)])  # (node, row, column)

        while queue:
            node, row, col = queue.popleft()
            node_data[col].append((row, node.val))

            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        result = []
        for col in sorted(node_data.keys()):
            result.append([val for row, val in sorted(node_data[col])])

        return result
