# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# RECURSIVE DFS
class Solution(object):
    """
    O(N)
    O(log N)
    """
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1




# Example Tree:
#        3
#       / \
#      9   20
#          /  \
#         15   7

def create_tree():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

# Test the Solution
tree = create_tree()
solution = Solution()
result = solution.maxDepth(tree)
print("Maximum depth of the tree:", result)  # Expected Output: 3




# ITERATIVE DFS
class Solution:
    """

    O(N)
    O(H)
    H: O(N) worst or O(log N) for balanced tree
    """

    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# BFS
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
