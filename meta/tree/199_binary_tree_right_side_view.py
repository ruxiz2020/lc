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
    level order traversal
    O(N)
    O(H)
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

lst = [1,2,3,None,5,None,4]
root = list_to_binary_tree(lst)
print(root)
res = Solution().rightSideView(root)
print(res)
