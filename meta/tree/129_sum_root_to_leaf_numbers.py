from typing import Optional


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


class Solution:
    """
    This code calculates the sum of all root-to-leaf numbers in a binary tree, 
    where each path from the root to a leaf node forms a number by 
    concatenating the values of the nodes along the path.

    It uses a Depth-First Search (DFS) approach, carrying a running "path value" 
    down the tree, updating the total sum (ans) when a leaf node is reached, 
    and recursively traversing left and right subtrees to accumulate the sums.

    The algorithm has a time complexity of 
    O(N), where 
    N is the number of nodes in the tree, as it visits each node once, 
    and a space complexity of 
    O(H), where 
    H is the height of the tree, due to the recursion stack.
    O(N)
    O(H)
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root: Optional[TreeNode], path: int) -> None:
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                print(path)
                ans += path * 10 + root.val
                return

            dfs(root.left, path * 10 + root.val)
            print(ans) # 12
            dfs(root.right, path * 10 + root.val)
            print(ans) # 25

        dfs(root, 0)
        return ans

lst = [1,2,3]
root = list_to_binary_tree(lst)

res = Solution().sumNumbers(root)
print(res) # 25
