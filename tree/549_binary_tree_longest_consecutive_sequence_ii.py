class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        # Path including root
        res = 1 + self.findPath(root, 1) + self.findPath(root, -1)
        # Compare with path excluding root
        return max(res, max(self.longestConsecutive(root.left), self.longestConsecutive(root.right)))

    # longest consecutive subtree containing root
    def findPath(self, node: TreeNode, diff: int) -> int:
        if not node:
            return 0

        left, right = 0, 0
        if node.left and node.val + diff == node.left.val:
            left = self.longestSubtree(node.left, diff) + 1
        if node.right and node.val + diff == node.right.val:
            right = self.longestSubtree(node.right, diff) + 1
        return max(left, right)


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self.dfs(root)[0]

    # Return the maxPath, incr, decr to node
    def dfs(self, node: TreeNode) -> (int, int, int):
        if not node:
            return (0, 0, 0)

        res, incr, decr = 1, 1, 1
        if node.left:
            left = self.dfs(node.left)
            if node.val + 1 == node.left.val:
                incr = left[1] + 1
            elif node.val - 1 == node.left.val:
                decr = left[2] + 1
            res = max(res, left[0])

        if node.right:
            right = self.dfs(node.right)
            if node.val + 1 == node.right.val:
                incr = max(incr, right[1] + 1)
            elif node.val - 1 == node.right.val:
                decr = max(decr, right[2] + 1)
            res = max(res, right[0])

        res = max(res, incr + decr - 1)
        return (res, incr, decr)
