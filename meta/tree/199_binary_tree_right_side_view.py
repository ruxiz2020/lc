# Definition for a binary tree node.
import collections
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binary_tree(lst):
    if not lst:
        return None

    # Create the root of the tree
    root = TreeNode(lst[0])
    queue = [root]  # Queue to hold nodes for assignment
    idx = 1  # Index to traverse the list

    while idx < len(lst):
        # Get the current parent node from the queue
        parent = queue.pop(0)

        # Assign left child if available
        if idx < len(lst) and lst[idx] is not None:
            parent.left = TreeNode(lst[idx])
            queue.append(parent.left)
        idx += 1

        # Assign right child if available
        if idx < len(lst) and lst[idx] is not None:
            parent.right = TreeNode(lst[idx])
            queue.append(parent.right)
        idx += 1

    return root

def print_tree(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result

class Solution:
    """
    We perform a level-order traversal (BFS) of the tree. At each level,
    we keep track of the rightmost non-null node encountered. That node's value
    represents the tree's "right side" view at that level.

    Time Complexity: O(N), where N is the total number of nodes,
      since each node is enqueued and dequeued exactly once.
    Space Complexity: O(H), where H is the maximum number of nodes at any level
      (i.e., the width of the tree at its widest point). Typically, H <= N.
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        # This list will store the rightmost value at each level
        res = []

        # Use a queue (deque) for the BFS; start with root
        q = collections.deque([root])

        # While there are nodes to process...
        while q:
            # We'll track the rightmost node in this level
            rightSide = None

            # Number of nodes in the current level
            qLen = len(q)

            # Process all nodes in the current level
            for _ in range(qLen):
                node = q.popleft()

                if node:
                    # Track the latest (rightmost) node in this level
                    rightSide = node

                    # Add children for the next level
                    q.append(node.left)
                    q.append(node.right)

            # If we found a rightmost node at this level, add it to the result
            if rightSide:
                res.append(rightSide.val)

        return res


lst = [1,2,3,None,5,None,4]
root = list_to_binary_tree(lst)
print(root)
res = Solution().rightSideView(root)
print(res)
